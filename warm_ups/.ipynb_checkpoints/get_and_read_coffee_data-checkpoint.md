### Download and Read in Coffee Data

1. Download the Coffee dataset directly from [here](http://www.timeseriesclassification.com/description.php?Dataset=Coffee)  

   - Click "Download this dataset"    
   - Extract to folder called `Coffee`  
   - Take a look at the `Coffee_TRAIN.txt` file  

2. Import the data into python.

   - You can start with this code snippet, where you'll need to modify `data_path`  

```
import numpy as np
import os

data_path = '/Users/youmisuk/Documents/datasets/Coffee/'
file_name = 'Coffee_TRAIN.txt'
full_path = os.path.join(data_path, file_name)

data = np.loadtxt(full_path, delimiter=',')
```

Q: What happens? Can you get it working?

  - It turns out that this program uses the same method for reading the data, and it breaks.