%The sample number to be plotted.
%Example : x = [2,3] will plot data for samples 2 and 3.
%          x = 7 will plot the data for sample 7

x = [2,3,4,6,7,8];

%Select which plot to make.
i = 1;
% 1 = T vs mu
% 2 = T vs n_s
% 3 = 1000/T vs n_s
% 4 = T vs V_h
% 5 = T vs R_s
% 6 = T vs log(R_s)


%Scan the data into matlab from a file made by Hall_calc.
a = 0;
for k = 1:length(x)
    skra = fopen(['Hall_data_for_ZnO_sample' num2str(x(k)) '.dat']);
    scanned{k} = textscan(skra, '%f %f %f %f %f %f %f %f %f %f %f','Headerlines',2);
    fclose(skra);
    
    %Finding the largest data range
    if a < max(length(scanned{k}{1}));
        a = max(length(scanned{k}{1}));
    end
end

%Pre-allocate to accomidate for different sizes of data.
Temperature = NaN(a,length(x));
V_h = NaN(a,length(x));
mu = NaN(a,length(x));
n_s = NaN(a,length(x));
R_s = NaN(a,length(x));

%Reading the data into variables.
for n = 1:length(x)
    range = 1:length(scanned{n}{1});
    Temperature(range,n) = scanned{n}{1};
    V_h(range,n) = scanned{n}{2};
    mu(range,n) = scanned{n}{3};
    n_s(range,n) = scanned{n}{4};
    R_s(range,n) = scanned{n}{5};
end

%Plot the data
clf
switch i
    case 1
        %%%%%%%%%%%
        % T vs mu %
        %%%%%%%%%%%
        plot(Temperature,mu,'.')
        xlabel('Temperature [K]')
        ylabel('\mu   [cm^2 / V s]')
        
    case 2
        %%%%%%%%%%%%
        % T vs n_s %
        %%%%%%%%%%%%
        plot(Temperature,n_s,'.')
        xlabel('Temperature [K]')
        ylabel('n_s  [cm^{-2}]')
        
    case 3
        %%%%%%%%%%%%%%%%%
        % 1000/T vs n_s %
        %%%%%%%%%%%%%%%%%
        plot(1000./Temperature,n_s,'.')
        xlabel('1000/T [K^{-1}]')
        ylabel('n_s  [cm^{-2}]')
             
    case 4
        %%%%%%%%%%%%
        % T vs V_h %
        %%%%%%%%%%%%
        V_h = V_h*1000;
        plot(Temperature,V_h,'.')
        xlabel('Temperature [K]')
        ylabel('V_H  [ mV ]')
        
    case 5
        %%%%%%%%%%%%
        % T vs R_s %
        %%%%%%%%%%%%
        plot(Temperature,R_s,'.')
        xlabel('Temperature [K]')
        ylabel('R_s  [\Omega]')
        
    case 6
        %%%%%%%%%%%%%%%%%
        % T vs log(R_s) %
        %%%%%%%%%%%%%%%%%
        semilogy(Temperature,R_s,'.')
        xlabel('Temperature [K]')
        ylabel('R_s  [\Omega]')
end

%Add legends the plot.
sample = {'ZnO', 'ZnO' , 'ZnO', 'ZnO' , 'ZnBeO', 'ZnBeO', 'ZnBeO', 'ZnBeO'};
annealed = {'', '600°C', '800°C', '900°C', '', '600°C', '800°C', '1000°C'};
leg = {};
for i = 1:length(x)
    leg{i} = [sample{x(i)} ' ' annealed{x(i)}];
end
legend(leg,'Location','best')


%Resize the plot window with option to output a pdf file with the plot.
%Uncomment the last 2 lines to output the pdf.
box on
set(gca, 'Position', get(gca, 'OuterPosition') - ...
    get(gca, 'TightInset') * [-1 0 1 0; 0 -1 0 1; 0 0 1 0; 0 0 0 1]);
set(gcf, 'renderer', 'painters');
set(gcf, 'PaperPosition', [-0.1 0 6.7 5]); 
set(gcf, 'PaperSize', [6.7 5]);
% pdf_name = 'Hall_Samp2_Sheet_res.pdf';
% print(gcf, '-dpdf', pdf_name);