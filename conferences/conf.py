import pandas as pd

df = pd.read_csv("./conferences/confs.csv", sep=";")

for ind, item in df.iterrows():
    with open(f"./_talks/conf_{ind}.md", "w+") as f:
        f.write("---\n")
        print(dict(item))
        newd = {}
        for k, v in dict(item).items():
            newd[k.strip()] = str(v).strip()
        for k, v in newd.items():
            f.write(f'{k}: "{v}"\n')
        f.write("collection: talks\n")
        f.write("---\n\n<!--  -->\n\n")

        if newd["abstract"].strip() in ["", "nan"]:
            pass
        else:
            if newd["abstract"].split(".")[-1] in ["md", "txt"]:
                for line in open(f"./files/talks/{newd['abstract']}", "r"):
                    f.write(line)
            else:
                # f.write(
                #     '<object data="{{site.author.baseurl}}/files/'+newd["abstract"]+'" width="800" height="900"> </object>')
                f.write(
                    '[Download abstract]({{site.author.baseurl}}/files/talks/'+newd["abstract"]+')')
