// Initialization
requires("1.53c");
run("Options...", "iterations=3 count=1 black edm=Overwrite");
run("Colors...", "foreground=white background=black selection=yellow");
run("Clear Results"); 
run("Close All");
close("Log");

// Data

setBatchMode(true);
start = getTime();

#@ File(label="Raw data:", value = "C:/", style="directory") input
#@ Integer(label="Background Subtraction:", value = 5, style="spinner") BGSub

input = input +"/";
files = getFileList(input);
files = ImageFilesOnlyArray(files);

File.mkdir(input + "Output");
output = input + "Output/"
// Loop over files

for (i = 0; i < files.length; i++) {
	open(input + files[i]);
	filename =  clean_title(files[i]);
	rename("Image");
	
	// Split channels
	run("Split Channels");
	selectWindow("C1-Image");
	
	run("Duplicate...", "title=Mask");
	
	// filter
	run("Median...", "radius=18 stack");
	
	// bg substract
	run("Subtract Background...", "rolling="+BGSub+" stack");
	
	//segmentation
	run("8-bit");
	run("Auto Local Threshold", "method=Bernsen radius=30 parameter_1=0 parameter_2=0 white");
	run("Set Measurements...", "area mean min integrated redirect=C2-Image decimal=3");
	run("Analyze Particles...", "  show=[Count Masks] display exclude clear in_situ");
	
	run("glasbey_on_dark");
	
	run("Merge Channels...", "c2=C1-Image c6=Mask create");
	
	saveAs("Results", output + "Cell_Counts_" + filename +".csv");
	save(output + filename + "merge.tif");
	
	close("*");
}

end = getTime();
time = end-start

print("Total time = " + time);

selectWindow("Log");
saveAs("txt", input+"/Analysis_Log.txt");

function ImageFilesOnlyArray (arr) {
	//pass array from getFileList through this e.g. NEWARRAY = ImageFilesOnlyArray(NEWARRAY);
	setOption("ExpandableArrays", true);
	f=0;
	files = newArray;
	for (i = 0; i < arr.length; i++) {
		if(endsWith(arr[i], ".tif") || endsWith(arr[i], ".nd2") || endsWith(arr[i], ".LSM") || endsWith(arr[i], ".czi") || endsWith(arr[i], ".jpg") ) {   //if it's a tiff image add it to the new array
			files[f] = arr[i];
			f = f+1;
		}
	}
	arr = files;
	arr = Array.sort(arr);
	return arr;
}

function clean_title(imagename){
	nl=lengthOf(imagename);
	nl2=nl-3;
	Sub_Title=substring(imagename,0,nl2);
	Sub_Title = replace(Sub_Title, "(", "_");
	Sub_Title = replace(Sub_Title, ")", "_");
	Sub_Title = replace(Sub_Title, "-", "_");
	Sub_Title = replace(Sub_Title, "+", "_");
	Sub_Title = replace(Sub_Title, " ", "_");
	Sub_Title = replace(Sub_Title, ".", "_");
	Sub_Title=Sub_Title;
	return Sub_Title;
}