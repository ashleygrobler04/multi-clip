# about multiClip
MultiClip is a tool that allows you to store more than 1 copied text item. It works simularly to the feature found on windows. The data is stored in a json file, called clipdata.json.
## How do I run this?
You need python installed, I used python 3.9. Then you need to install clipboard and wxpython:
* pip install wxpython
* pip install clipboard
then just cd into the directory and run "python app.py"

## How does this work?
If you open up the app for the first time, you will see a list and 2 buttons. The list will be empty since there is no data to load. Make sure you have something important on your clipboard you don't want to have lost, then press the "Save" button.
Then you will be presented with an input box asking for a key. A key in this context is basicly a short description of the text you want to save. For example if I have the whole alphabet on my clipboard and I want to save it to retreive it for later use, my key would be "alphabet" without the quoats.
When you're done, press enter or ok. Then you will see a list that contains the key that you've entered. You need to remember whitch key contains whitch information. But that shouldn't be too hard...
You can copy the stored item by selecting it's key from the list and clicking on the "Copy" 
button. It will copy the text to the clipboard.
Please note: you need to select a key from the list else nothing will be copied to the clipboard.
## Notes
1. I know the GUI looks bad at this stage, but I'll try to improove on it when I get time.
2. I am planning to add a delete button so that you can get rid of items you no longer want to store or retreive for future use.
3. Any pull requests are welcome!
I hope you find this tool useful. If you have any questions, feel free to send me [An E Mail](ashleygrobler04@gmail.com)
