%Reads and plots a data file from the Hall_calc 
skra = fopen('Hall_data_for_ZnO_sample4.dat');
lesid = textscan(skra, '%f %f %f %f %f %f %f %f %f %f %f','Headerlines',2);
fclose(skra);
Temperature = lesid{1};
V_h = lesid{2};
mu = lesid{3};
n_s = lesid{4};
R_s = lesid{5};
Uni_test = [lesid{6}, lesid{7}, lesid{8}, lesid{9}, lesid{10}, lesid{11}];


%Select which plot to make.
i = 6;
% 1 = T vs mu
% 2 = T vs n_s
% 3 = 1000/T vs n_s
% 4 = T vs V_h
% 5 = T vs R_s
% 6 = T vs Uniform test

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
        %%%%%%%%%%%%%%%%%%%%%
        % T vs Uniform test %
        %%%%%%%%%%%%%%%%%%%%%
        hold on
        plot(Temperature,Uni_test,'.-')
        plot([min(Temperature), max(Temperature)], [0,0],'-.k')
        legend('Test1', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6')
        Current_ylim = ylim;
        ylim([-0.1, Current_ylim(2)])
        xlabel('Temperature [K]')
        ylabel('Deviation  [%]')
        hold off
end


%Resizes the plot window with option to output a pdf file with the plot.
%Uncomment the last 2 lines to output the pdf.
box on
set(gca, 'Position', get(gca, 'OuterPosition') - ...
    get(gca, 'TightInset') * [-1 0 1 0; 0 -1 0 1; 0 0 1 0; 0 0 0 1]);
set(gcf, 'renderer', 'painters');
set(gcf, 'PaperPosition', [-0.1 0 6.7 5]); 
set(gcf, 'PaperSize', [6.7 5]);
% pdf_name = 'Hall_Samp2_Sheet_res.pdf';
% print(gcf, '-dpdf', pdf_name);