% Get list of all files in this directory
% diary('DataBad\outputBad.txt');
% diary on;
diary('ini.txt');
diary on;

imagefiles1 = dir('hasilcek\*.jpg'); 
nfiles1 = length(imagefiles1);     % total number of files found
for ii=1:nfiles1  % loop for each file 
   currentfilename = imagefiles1(ii).name;  
   currentimage = double(imread(['hasilcek\',currentfilename]));
   nlevel{ii} = NoiseLevel(currentimage);
     fprintf(currentfilename);
     fprintf(' : ');
     fprintf(' %f',nlevel{ii});
     fprintf('\n');
end
diary off;



