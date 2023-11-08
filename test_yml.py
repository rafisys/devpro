import yaml

with open('first.yaml','r') as file :
        print(yaml.safe_load(file))
    except yaml.YAMLError as exc:
        print(exc)   
        
vvdjrdjgycvhgvnbmvn m