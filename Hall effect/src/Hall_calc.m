%Configure the current and magnetic field, filename and temperature.
I = 1e-3;
B = 1*1e-4;   %Tesla converted to gauss
name = 'graphene_ve';
Temperature = [5:10:305,310];


%Pre-allocate
V24p = zeros(1,length(Temperature));
V24n = zeros(1,length(Temperature));
V42p = zeros(1,length(Temperature));
V42n = zeros(1,length(Temperature));
V31p = zeros(1,length(Temperature));
V31n = zeros(1,length(Temperature));
V13p = zeros(1,length(Temperature));
V13n = zeros(1,length(Temperature));
R_s = zeros(1,length(Temperature));
Uni_test = zeros(length(Temperature),7);

channels = {'ch1','ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11', 'ch12'};

for i = 1:length(Temperature)
    scanned = {};
    %Check if all files are ok, and have the format ( 0, B, -B, 0 )
    file_error = 0;
    for k = 1:12
        filename = [channels{k} '_T' num2str(Temperature(i)) '_00' name '.dat'];
        skra = fopen(filename,'r');
        scanned = textscan(skra, '%f %f %f %f %f %f %f %f %f','headerlines',1);
        fclose(skra);
        
        %The error checks
        if length(scanned{1}) ~= 4
            file_error = 1;
            break
        elseif scanned{1}(1) ~= 0
            file_error = 1;
            break
        elseif abs(scanned{1}(2) - B) < 0.05
            file_error = 1;
            break
        elseif abs(scanned{1}(3) + B) < 0.05
            file_error = 1;
            break
        elseif scanned{1}(4) ~= 0
            file_error = 1;
            break
        end
    end
    
    %If error found, skip temperature and print a message
    if file_error == 1
        disp(['file for ' channels{k} ' and temperature ' num2str(Temperature(i)) ' needs checking.'])
        continue
    end
    scanned = {};

    %Scan hall channels for the current temperature
    for j = 1:4
        filename = [channels{j} '_T' num2str(Temperature(i)) '_00' name '.dat'];
        skra = fopen(filename,'r');
        scanned{j} = textscan(skra, '%f %f %f %f %f %f %f %f %f','headerlines',1);
        fclose(skra);
    end
    
    %Assign values based on channels    
    V13p(i) = scanned{1}{4}(2);
    V13n(i) = scanned{1}{4}(3);
    V31p(i) = scanned{2}{4}(2);
    V31n(i) = scanned{2}{4}(3);
    V42p(i) = scanned{3}{4}(2);
    V42n(i) = scanned{3}{4}(3);
    V24p(i) = scanned{4}{4}(2);
    V24n(i) = scanned{4}{4}(3);
    
    Uni_test(i,1) = Temperature(i);
    %Calculate the sheet resistivity.
    [R_s(i), Uni_test(i,2:7)] = Sheet_Res(name,Temperature(i));
    
    Temperature(i) = mean(mean([scanned{1}{7}, scanned{2}{7}, scanned{3}{7}, scanned{4}{7}]));
end

%Calculate the Hall voltage.
V_c = V24p - V24n;
V_d = V42p - V42n;
V_e = V13p - V13n;
V_f = V31p - V31n;
V_H = (V_c + V_d + V_e + V_f)/8;

%Calculate the carrier density.
if V_H > 0
    p_s = I*B./(1.602e-19*V_H);
    n_s = zeros(size(p_s));
else
    n_s = I*B./(1.602e-19*abs(V_H));
    p_s = zeros(size(n_s));
end

%Calculate the mobility.
mu = 1./(1.602e-19*max(p_s,n_s).*R_s);

%Write all the data to a file.
filename2 = ['Hall_data_for_' name '.dat'];
skra = fopen(filename2,'w');
fprintf(skra,'%s %1.2e %s %2.1f %s \r\n','Measurement done with I =', I, '[A] and B at +/-', B*1e4, '[T].');
fprintf(skra,'%s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \r\n', ...
    'Temperature', 'V_h', 'Mu', 'Carrier', 'R_s', ...
    'Uni_test1', 'Uni_test2', 'Uni_test3', 'Uni_test4', 'Uni_test5', 'Uni_test6');
for i = 1:length(Temperature)
    fprintf(skra,'%3.3f\t%1.5e\t%4.2f\t%1.6g\t%5.2f \t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t%2.4f\t \r\n',...
        Temperature(i), V_H(i), mu(i), max(n_s(i),p_s(i)), R_s(i), ...
        Uni_test(i,2), Uni_test(i,3), Uni_test(i,4), Uni_test(i,5), Uni_test(i,6), Uni_test(i,7));
end
fclose(skra);