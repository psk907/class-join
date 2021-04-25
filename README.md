# class-join

*Python script that automatically launches the class URL from the **data.json** file.*

## Usage Instructions
1. Clone the repository

    `git clone https://github.com/psk907/class-join.git`
    
2. Install dependencies

    `pip install pyautogui`

3. Fill your links in the **data.json**
    
    ```
    {
    "links":{
        "mon":[
            "https://your-class-link",
            "tbd", //when the link isnt available
            "impartus", //to join on Impartus   ...
        ],  ...
        }
     }
     ```

4. Run the script
    
    `python app.py`
