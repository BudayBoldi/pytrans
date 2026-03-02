import asyncio
from googletrans import Translator, constants

file = "sample.srt"
subtitle = 1

async def GTransText(sub):
    async with Translator() as translator:
        with open(file, "r") as ofile:
            newfile = file.split(".")

            with open(newfile[0] + "_en." + newfile[1], "w") as onewfile:
                while True:
                    line = ofile.readline()
                    
                    if sub == 3:
                        converted = await translator.translate(line)
                        print(converted.text)
                        onewfile.write(converted.text)
                        sub = 0
                    else:
                        onewfile.write(line)
                    
                    if line != "" and line !="\n" and line !="\r\n" and line !="\r":
                        sub += 1
                    
                    if not line:
                        break
                    
                
            
        
    
asyncio.run(GTransText(subtitle))