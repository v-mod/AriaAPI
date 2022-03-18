import AriaAI
def check(statement):
    if 'wikipedia' in statement:
        result = AriaAI.search_wikepedia(statement)
        return '_'+result

    elif "weather" in statement:
        weather=AriaAI.get_weather(statement)
        return '_'+weather

    elif 'who made you' in statement or 'who are you' in statement or 'what are you' in statement or 'when were you made' in statement:
        return'_Hi, My name is Aria and I was made by Vivaan Modi. I am an AI Assistant powered by the internet of things. You can ask me any question you like. I was born in March 2021'
        
    elif ' time' in statement and 'times' not in statement:
        return '_'+AriaAI.get_time()
    
    elif 'email' in statement:
        return'web.open-https://outlook.live.com_opening outlook'

    elif 'music' in statement:
        return'web.open-https://open.spotify.com/_Here is Spotify Web'

    elif 'news' in statement:
        return'web.open-https://bbc.com/_Here are some headlines from the BBC, Happy reading'

    elif 'search bing'  in statement:
        statement = statement.replace("search bing", "")
        return'web.open-https://www.bing.com/search?q='+statement+'_Ok, opening bing'

    elif 'search youtube'  in statement:
        statement = statement.replace("search youtube", "")
        return'web.open-https://www.youtube.com/results?search_query='+statement+'_Ok, searching youtube'

    elif "photo" in statement:
        return 'photo-take_Ok, taking a photo of you now'

    elif 'exit' in statement:
        return'exit_ok, exiting now'
    
    elif 'search google'in statement:
        statement = statement.replace("search google", "")
        return'web.open-https://www.google.com/search?q='+statement+'_Ok, opening google'

    elif 'open app' in statement:
        statement = statement.replace("open app", "")
        return statement+'.open_ok, opening it now'

    elif 'assistant' in statement:
        return '_'+'My mortal enemy is Siri but i dont mind Google, Alexa and cortana'

    elif 'play' in statement or 'pause' in statement:
        return 'play-pause_ok, doing it now'
    
    elif 'volume up' in statement:
        return 'vol-up_Ok, increasing volume'

    elif 'volume down' in statement:
        return 'vol-down_Ok, increasing volume'

    elif 'why ' in statement or 'what ' in statement or 'where ' in statement or 'who ' in statement or 'how ' in statement or 'when ' in statement: 
        return '_'+AriaAI.ask_Aria(statement)

    elif 'joke' in statement:
        return '_'+AriaAI.tell_me_a_joke()
    

    else: 
        return "_"