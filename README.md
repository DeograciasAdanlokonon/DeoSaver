# DeoSaver
The program is an Automatic File Saving Utility with a graphical user interface (GUI) developed using the Tkinter library in Python. This utility is designed to automate the process of saving files in specific editor software applications.
**DeoSaver Description: Automatic File Saving Utility**

**Introduction:**
The program is an Automatic File Saving Utility with a graphical user interface (GUI) developed using the Tkinter library in Python. This utility is designed to automate the process of saving files in specific editor software applications.

**Key Features:**

1. **Start and Stop Buttons:** The program's GUI consists of two buttons, a green "Start" button, and a red "Stop" button.

2. **Confirmation Messages:** When you click either the "Start" or "Stop" button, the program displays a confirmation message indicating whether the action was executed successfully.

3. **Editor Software Filter:** The program is tailored to interact with and save files in specific editor software applications. It filters open windows based on predefined keywords associated with popular text editors such as "Notepad", "Sublime Text", "Visual Studio Code", "Atom", "TextEdit", "VSCode", "Vim", "Emacs", "Word", "Excel", "PowerPoint", "Publisher", "Access", "Adobe Photoshop", "Adobe Illustrator" and "Adobe Indesign".

4. **Automatic File Saving:** Once the "Start" button is clicked, the program continuously scans for open windows matching the editor software keywords. For each matching window, it simulates the CTRL+S keyboard shortcut to save the files, ensuring that any unsaved changes are preserved.

5. **User-Controlled Stop:** Users can stop the automatic file-saving process at any time by clicking the "Stop" button. The program responds by immediately ceasing its automatic file-saving activity.

**Usage Instructions:**

1. **Start Button:** To initiate the automatic file-saving process, click the green "Start" button. The program will start scanning and saving files in editor software windows that match the predefined keywords.

2. **Stop Button:** To stop the automatic file-saving process, click the red "Stop" button. The program will immediately halt its scanning and saving activity.

3. **Confirmation Messages:** Each time you click the "Start" or "Stop" button, a confirmation message will appear, notifying you that the respective action has been executed successfully.

4. **Editor Software Interaction:** The program will interact exclusively with windows belonging to editor software applications. It identifies these windows by checking their titles against a list of predefined keywords associated with such software.

5. **Customization:** You can customize the list of editor software keywords in the script to include additional software titles you want the program to target.

**Important Considerations:**

- **System Resources:** Continuous automation may consume system resources, so ensure that your computer can handle the program's operation effectively.

- **Editor Software Keywords:** Modify the list of editor software keywords to include the titles of the specific software you want to target.

- **Responsible Use:** Automate tasks responsibly and ethically, respecting the privacy and security of the systems you interact with.

DeoSaver is a valuable utility for users who frequently work with text editors and want to automate the process of saving files to ensure that their work is regularly preserved without manual intervention.
