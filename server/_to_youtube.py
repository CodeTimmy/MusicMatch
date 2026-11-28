import yt_dlp
import json

def to_youtube(file, name):
    with open(file, 'r', encoding='utf-8') as f:
        input = json.load(f)
        output = []
        for input["songs"] as song_name:
            with yt_dlp.YoutubeDL({"quiet": True, "extract_flat": True}) as ydl:
                info = ydl.extract_info(f"ytsearch3:{song_name}", download=False)
                result = info["entries"][0]:
                print(result["title"], result["id"])
                output.append(result["id"])
    output_json = {"ids": output}
    with open(f"youtube/{name}.json", 'w', encoding='utf-8') as f:
        json.dump(output_json, f, indent=4, ensure_ascii=False)
    return output_json
