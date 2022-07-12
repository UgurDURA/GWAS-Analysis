import asyncio
import panel as pn
from panel.io.pyodide import show
import sys
from js import alert, document, Object, window
from pyodide import create_proxy, to_js

file_input = pn.widgets.FileInput(accept = ".csv", width = 180)
button_upload = pn.widgets.Button(name = 'Upload', button_type = 'primary', width = 100)
row = pn.Row(file_input, button_upload, height = 75)

async def file_save(event):
	# Note: print() does not work in event handlers

	try:
		options = {
			"startIn": "documents",
			"suggestedName": "Sample.vcf"
		}

		fileHandle = await window.showSaveFilePicker(Object.fromEntries(to_js(options)))
	except Exception as e:
		console.log('Exception: ' + str(e))
		return

  
  
	content = document.getElementById("myFile").value

	file = await fileHandle.createWritable()
	await file.write(content)
	await file.close()
	return

def setup_button():
	# Create a Python proxy for the callback function
	file_save_proxy = create_proxy(file_save)

	# Set the listener to the callback
	document.getElementById("file_save").addEventListener("click", file_save_proxy, False)

setup_button()


# async def file_save(event):
# 	# Note: print() does not work in event handlers

# 	try:
# 		options = {
# 			"startIn": "documents",
# 			"suggestedName": "testfile.txt"
# 		}

# 		fileHandle = await window.showSaveFilePicker(Object.fromEntries(to_js(options)))
# 	except Exception as e:
# 		console.log('Exception: ' + str(e))
# 		return

# 	content = file_input.value

# 	file = await fileHandle.createWritable()
# 	await file.write(content)
# 	await file.close()
# 	return

# def setup_button():
# 	# Create a Python proxy for the callback function
# 	file_save_proxy = create_proxy(file_save)

# 	# Set the listener to the callback
# 	document.getElementById("file_save").addEventListener("click", file_save_proxy, False)

# setup_button()

button_upload.on_click()

await show(row, 'fileInput')


 