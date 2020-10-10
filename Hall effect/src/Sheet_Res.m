function [R_s, Uni_test] = Sheet_Res(name,Temperature)
%Calculates the sheet resistance.

scanned = {};
channels = {'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11', 'ch12'};

for i = 1:8
    filename = [channels{i} '_T' num2str(Temperature) '_00' name '.dat'];
    skra = fopen(filename,'r');
    scanned{i} = textscan(skra, '%f %f %f %f %f %f %f %f %f','headerlines',1);
    fclose(skra);
end

%Pick out the rows where B = 0.
x = 1:3:4;
Ch5 = mean(scanned{1}{5}(x));
Ch6 = mean(scanned{2}{5}(x));
Ch7 = mean(scanned{3}{5}(x));
Ch8 = mean(scanned{4}{5}(x));
Ch9 = mean(scanned{5}{5}(x));
Ch10 = mean(scanned{6}{5}(x));
Ch11 = mean(scanned{7}{5}(x));
Ch12 = mean(scanned{8}{5}(x));

%Uniformity Tests
Test1 = abs(Ch5/Ch6 - 1)*100;
Test2 = abs(Ch7/Ch8 - 1)*100;
Test3 = abs(Ch9/Ch10 - 1)*100;
Test4 = abs(Ch11/Ch12 - 1)*100;

CCh1 = Ch5 + Ch6;
CCh2 = Ch7 + Ch8;
CCh3 = Ch9 + Ch10;
CCh4 = Ch11 + Ch12;

Test5 = abs(CCh1/CCh3 - 1)*100;
Test6 = abs(CCh2/CCh4 - 1)*100;

Uni_test = [Test1, Test2, Test3, Test4, Test5, Test6];




R_A = (Ch5 + Ch6 + Ch9 + Ch10)/4;
R_B = (Ch7 + Ch8 + Ch11 + Ch12)/4;

%Calculate R_s from R_A and R_B
delta = 0.0005;
err = 100;
i = 0;
Z_old = 2*log(2)/(pi*(R_A + R_B));
while err > delta
    i = i + 1;
    y_i = 1/exp(pi*Z_old*R_A) + 1/exp(pi*Z_old*R_B);
    Z_new = Z_old - ((1-y_i)/pi)/( R_A/exp(pi*Z_old*R_A) + R_B/exp(pi*Z_old*R_B) );
    
    err = (Z_new - Z_old)/Z_new;
    Z_old = Z_new;
end
R_s = 1/Z_new;