    speech = listener.listen(origin)
        intruction = listener.recognize_google(speech)
        print(intruction)