%Select which data to plot.

i = 10;
% 1 = Sample1 band edge
% 2 = Sample1 deep end
% 3 = Sample2 band edge
% 4 = Sample2 deep end
% 5 = Sample3 band edge
% 6 = Sample3 deep end
% 7 = Sample4 band edge
% 8 = Sample4 deep end
% 9 = Sample4 old deep end
% 10 = Sample5 band edge
% 11 = Sample5 deep end
% 12 = Sample6 band edge
% 13 = Sample6 deep end
% 14 = Sample7 band edge
% 15 = Sample7 deep end
% 16 = Sample8 band edge
% 17 = Sample8 deep end

scanned = {};
intens = [];
clf
switch i
    case 1
        Temperature = [12, 15, 20:10:40, 60:20:100, 130, 160, 200, 235, 270, 300];
        scanned = Read_Temp('samp1','340-400nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        intens = intens - min(min(intens)) + 1;
        lambda = scanned{1}{1};
        
        semilogy(lambda, intens)
        xlim([338,402])
        
    case 2
        
        Temperature = [12, 15:5:25, 30:10:50, 70:20:210, 240:30:300];
        scanned = Read_Temp('samp1','400-1000nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        
        plot(lambda,intens)
        xlim([390,1010])
        
    case 3
        
        Temperature = [12:2:20, 25:5:80, 90:10:150, 170:20:190, 220, 250, 300];
        scanned = Read_Temp('samp2','360-440nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        intens = intens - min(min(intens)) + 1;
        lambda = scanned{1}{1};
    
        semilogy(lambda, intens)
        xlim([358,442])
    
    case 4
        
        Temperature = [12:2:20, 25:5:35, 50:20:190, 220, 250, 300];
        scanned = Read_Temp('samp2','400-1000nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        
        plot(lambda,intens)
        xlim([390,1010])
        
    case 5
        
        Temperature = [12:2:16];
        scanned = Read_Temp('samp3','350-450nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        intens = intens - min(min(intens)) + 1;
        lambda = scanned{1}{1};
        
        %Gain setting 1
        intens = intens*4;
        
        Temperature = [18, 20, 25:5:80, 90:10:150, 170:20:250, 275, 300];
        scanned2 = Read_Temp('samp3','355-450nm',Temperature);
        
        for j = 1:length(Temperature)
            intens2(:,j) = scanned2{j}{2};
        end
        intens2 = intens2 - min(min(intens2)) + 1;
        lambda2 = scanned2{1}{1};
        
        %Gain setting 1 for 12K-20K
        intens2(:,1:2) = intens2(:,1:2)*4;
        %Gain setting 2 for 25K-30K
        intens2(:,3:4) = intens2(:,3:4)*2;
        
        semilogy(lambda, intens, lambda2, intens2)
        xlim([353,452])
        
    case 6
        
        Temperature = [12, 15, 20:5:30, 40:10:90, 110:20:210, 240:30:300];
        scanned = Read_Temp('samp3','400-1000nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        
        plot(lambda,intens)
        xlim([390,1010])
        
    case 7
        
        Temperature = [12:2:20, 25:5:60, 70:10:150, 170:20:270];
        scanned = Read_Temp('samp4','360-410nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        intens = intens - min(min(intens)) + 1;
        lambda = scanned{1}{1};
        
        
        %Adding the point at 300K which has different wavelengths
        scanned = Read_Temp('Samp4','355-435nm',300);
        intens2 = scanned{1}{2};
        intens2 = intens2 - min(min(intens2)) + 1;
        lambda2 = scanned{1}{1};
                
        semilogy(lambda, intens, lambda2, intens2)
        xlim([358,412])
        
    case 8
        
        Temperature = [12, 15, 20:5:30, 40:10:80, 100:20:180, 210:30:300];
        scanned = Read_Temp('samp4','400-1000nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        
        plot(lambda,intens)
        xlim([390,1010])
        
    case 9
        
        Temperature = [12:2:20, 25:5:45, 60:10:150, 170:20:270, 300];
        scanned = Read_Temp('samp4_old','400-1000nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        
        plot(lambda,intens)
        xlim([390,1010])
        
    case 10
        
        Temperature = [12, 15, 20:5:30, 40:10:80, 100:20:180, 210:30:300];
        scanned = Read_Temp('Samp5','338-400nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        intens = intens - min(min(intens)) + 1;
        lambda = scanned{1}{1};
    
        semilogy(lambda, intens)
        xlim([336,402])
        
    case 11
        
        Temperature = [12, 15, 20:5:30, 40:10:80, 100:20:220, 240:30:300];
        scanned = Read_Temp('samp5','400-1000nm',Temperature);
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        
        plot(lambda,intens)
        xlim([390,1010])
        
    case 12
        
        Temperature = [12, 15, 20:5:30, 40:10:80, 100:20:180, 210:30:300];
        scanned = Read_Temp('Samp6','338-420nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        intens = intens - min(min(intens)) + 1;
        lambda = scanned{1}{1};
    
        semilogy(lambda, intens)
        xlim([336,422])
        
    case 13
        
        Temperature = [12, 15, 20:5:30, 40:10:80, 100:20:180, 220:40:300];
        scanned = Read_Temp('samp6','400-1000nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        
        plot(lambda,intens)
        xlim([390,1010])
        
    case 14
        
        Temperature = [12:2:20, 25:5:70, 80:10:100, 120:20:220, 250, 275, 300];
        scanned = Read_Temp('samp7','350-400nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        intens = intens - min(min(intens)) + 1;
        
        semilogy(lambda, intens)
        xlim([348,402])
        
    case 15
        
        Temperature = [12:2:20, 25, 30:10:60, 80:20:220, 250, 275, 300];
        scanned = Read_Temp('samp7','400-1000nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        
        plot(lambda,intens)
        xlim([390,1010])
        
    case 16
        
        Temperature = [12, 15, 20:5:30, 40:10:80, 100:20:180, 210:30:300];
        scanned = Read_Temp('samp8','355-440nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        intens = intens - min(min(intens)) + 1;
        
        semilogy(lambda, intens)
        xlim([353,442])
        
    case 17
        
        Temperature = [12, 15, 20:5:30, 40:10:80, 100:20:180, 210:30:300];
        scanned = Read_Temp('samp8','400-1000nm',Temperature);
        
        for j = 1:length(Temperature)
            intens(:,j) = scanned{j}{2};
        end
        lambda = scanned{1}{1};
        
        plot(lambda,intens)
        xlim([390,1010])
        
end

xlabel('Wavelength [nm]')
ylabel('Intensity [a.u.]')

%Resize the plot window with option to output a pdf file with the plot.
%Uncomment the last 2 lines to output pdf.
box on
set(gca, 'Position', get(gca, 'OuterPosition') - ...
    get(gca, 'TightInset') * [-1 0 1 0; 0 -1 0 1; 0 0 1 0; 0 0 0 1]);
set(gcf, 'renderer', 'painters');
set(gcf, 'PaperPosition', [-0.15 0 6.7 5]);
set(gcf, 'PaperSize', [6.7 5]);
% pdf_name = 'TEST2';
% print(gcf, '-dpdf', pdf_name);
