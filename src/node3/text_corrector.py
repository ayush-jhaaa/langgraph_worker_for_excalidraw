# line height ≈ font size × line-height factor
# Use different average width multipliers per font:
    # Font 1 (Virgil): 0.65 × font size
    # Font 2 (Sans): 0.55 × font size
    # Font 3 (Mono): 0.6 × font size
    # Font 4 (Comic): 0.58 × font size

font_family_factor = {
        1: 0.65, 
        2: 0.55,  
        3: 0.60,  
        4: 0.58,  
}
def width_checker(json):
    # check if sufficient width is given or not
    width = json["width"]

    width_factor = font_family_factor[json["fontFamily"]]
    char_width = width_factor * json["fontSize"]
    min_width_needed = char_width * max(len(word) for word in json["text"].split(" ")) + 20
    # if width > min_width_needed: -> then good to go
    if width < min_width_needed:
        json["width"] = min_width_needed + 20 # idk but take 20 pixels more
    print(min_width_needed)

def line_breaker(json):
    # first put \n's then give apprprite height
    width_factor = font_family_factor[json["fontFamily"]]
    char_width = width_factor * json["fontSize"]
    max_width_allowed = json["width"] - 20 # 20 pixel -> 10,10 for padding
    text = json["text"]
    output = ""
    curr_width = 0

    # for height 
    number_of_lines = 1 #currently we only have one line

    for word in text.split(" "):
        if curr_width + (len(word)*char_width) > max_width_allowed:
            output += "\n" + word + " "
            curr_width = (len(word)*char_width)
            number_of_lines += 1

        else :
            output += word + " "
            curr_width += len(word)*char_width
    
    json["text"] = output.strip()
    print(f"number of lines = {number_of_lines}")

    line_height = json["fontSize"] * 1.25 #i will go with default lineHeight value = 1.25
    json["height"] = (number_of_lines * line_height) + 30 + (number_of_lines * 2) # 30 -> 15,15 padding plus 2pixel padding per line

def detect_text_align(text: str) -> str:
    """
    Decide alignment automatically.
    - center (paragraphs)
    - left (lists, code-like, or multiline bullets)
    """
    # on god it is what it is
    lines = text.strip().split("\n")
    num_lines = len(lines)

    # If multiple short lines -> bullet or list
    if num_lines > 1:
        avg_len = sum(len(l.strip()) for l in lines) / num_lines
        variance = sum(abs(len(l.strip()) - avg_len) for l in lines) / num_lines

        # bullet points or uneven line lengths
        if variance > 10 or text.strip().startswith(("-", "*", "•", "1.", "a.")):
            return "left"
        else:
            return "center"
    else:
        # Single line or long text = paragraph
        if len(text) > 40:
            return "center"
        return "left"


sample_json = {
  "type": "text",
  "id": "my-text-element",
  "x": 100,
  "y": 100,
  "autoResize": False,
  "version": 321124,
  "width": 250,
  "height": 126,
  "fontSize": 25,
  "fontFamily": 1,
  "text": "hello - kill -hjj -gev",
  "originalText": "Why did the scarecrow win an award for standing out in his field because lorem ipsum have agsugagrsajbngagbhfgabfahggd hbchagbisrbhbhbacsahb afvhcbjhb",
  "textAlign": "center",
  "verticalAlign": "middle"
}

width_checker(sample_json)
print(sample_json["width"])
line_breaker(sample_json)
sample_json["textAlign"] = detect_text_align(sample_json["text"])
print(sample_json["text"],sample_json["height"],sample_json["textAlign"])