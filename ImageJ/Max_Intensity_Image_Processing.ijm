data = "C:/Users/anaca/PycharmProjects/automation-scripts/data/fiji-automation/1_Neuron_Zstack/"

files = getFileList(data);
files = ImageFilesOnlyArray(files);

File.mkdir(data + "MaxIP");
output = data + "MaxIP/"

setBatchMode(true);

start = getTime();

for (i = 0; i < files.length; i++) {
	open(data + files[i]);

	run("Subtract Background...", "rolling=15 stack");
	
	run("Z Project...", "projection=[Max Intensity]");
	
	save(output + "MIP_"+ files[i]);
	
	close("*");
}

end = getTime();

time = end-start

print("Total time = " + time);

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