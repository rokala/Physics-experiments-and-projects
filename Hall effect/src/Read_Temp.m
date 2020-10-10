function scanned = Read_Temp(name, range, Temperature)
%Reads photoluminescense files that have the filename format
% 'name'_'range'_'Temperature'K.txt
%and returns a cell array with the data.

%Pre-allocate
scanned = cell(1,length(Temperature));

for i = 1:length(Temperature)
    filename = [name '_' range '_'  num2str(Temperature(i)) 'K' '.txt'];
    skra = fopen(filename,'r');
    scanned{i} = textscan(skra, '%f %f','headerlines',1);
    fclose(skra);
end
end