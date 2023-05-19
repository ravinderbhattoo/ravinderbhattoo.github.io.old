import pandas as pd
from slugify import slugify

df = pd.read_csv("./gen_publication/pubs.csv", sep=",")

print(df)
print(df.columns)

for ind, item in df.iterrows():
    filename = slugify(item['Title'])
    with open(f"./_publications/{filename}.md", "w+") as f:
        f.write("---\n")
        newd = {}
        for k, v in dict(item).items():
            newd[k.strip().replace(" ","_").lower()] = str(v).strip()
        if newd["item_type"] == "preprint":
            newd["venue"] = "Preprint"
        for k, v in newd.items():
            if k=="date":
                v = str(item["Publication Year"])+"-01-01"
            if k=="author":
                k = "authors"
            if k == "publication_title" and v!="nan":
                k = "venue"
            if k=="conference_name" and v!="nan":
                k = "venue"
            if k=="url":
                k = "paperurl"
            f.write(f'{k}: "{v}"\n')
        f.write("collection: publications\n")
        f.write("---\n\n")
        f.write("\n\n<!--  -->\n\n")

        f.write("{{ page.abstract_note }}\n\n")
        f.write("__Keywords__: {{ page.automatic_tags }}\n\n")
        f.write(f"[Dowonload paper here]({newd['url']})\n\n")
    #     if newd["abstract"].strip() in ["", "nan"]:
    #         pass
    #     else:
    #         f.write(newd["abstract"])


