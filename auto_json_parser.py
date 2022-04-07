import json


def json_manual_parser(text_string, output="json"):
    j = text_string.replace("{","").replace("}","").split(",")
    previous = ""
    good_list = []
    good_dict = {}
    for i in range(len(j)):
        try: 
            linted = ast.literal_eval("{"+j[i]+"}")
            good_list.append(linted)
            k = str(list(linted.keys())[0])
            v = re.sub(r"[\\|\'|\"]", "", str(linted[k]))
            good_dict[k] = v

        except:
            try:
                linted = ast.literal_eval( "{"+j[i-1]+"}" + "," + "{"+j[i]+"}" )
            except:
                try:
                    linted = ast.literal_eval( "{"+j[i-2]+"}" + "{"+j[i-1]+"}" + "," + "{"+j[i]+"}" )
                except:
                    pass

    dict_string = str(good_dict).replace("'", '"')
    
    if output=="json":
        return json.loads(dict_string)
    else: 
        return json.dumps(json.loads(dict_string), indent=4)
