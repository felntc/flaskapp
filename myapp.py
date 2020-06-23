from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import urllib
import numpy as np
import pandas as pd
from io import BytesIO

app = Flask(__name__)

#データフレームを加工する
df=pd.read_csv('03.csv', index_col=0 ,keep_default_na=False)
del df["Unnamed: 12"]

names=df.columns
for x in names:
    df[x]=df[x].str.replace(',', '').astype(int) #数字へ変換

#図示用のラベルを作成
labels=list(np.arange(100,1100,100))+[1500,2000,2500,2501]

#図示用に辞書を作成
x=np.arange(20,31)
obj=labels
dic0={i:j for i,j in zip(obj,np.arange(14))}
#fig = plt.figure(figsize=(20,8))
#fig, ax = plt.subplots(1,1)

@app.route("/")
def index():
    return render_template("index0.html")

@app.route("/plot/all")
def plot_all():
    dic=dic0.copy()
    fig, ax = plt.subplots(1,1)

    # Obtain query parameters
    start = int(request.args.get("start", type=str))-1988
    end = int(request.args.get("end", type=str))-1988

    if start > end:
        start, end = end, start
    #if (start + timedelta(days=7)) > end:
        #end = start + timedelta(days=7)

    png_1 = BytesIO()
    #dic=dic0.copy()
    for n,m in dic.items():
        dic[n]=df.iloc[m].values
        plt.plot(x,dic[n],label=n)
    ax.set_title("salary distribution")
    ax.set_xlabel("Heisei")
    ax.set_ylabel("people(thousands)")
    plt.grid(True)
    ax.legend()
    ax.set_xlim([start, end])
    #plt.xticks(rotation=30)

    plt.savefig(png_1, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_1.getvalue())

    return "data:image/png:base64," + img_data


@app.route("/area/all")
def area_all():
    dic=dic0.copy()
    fig, ax = plt.subplots(1,1)
    # Obtain query parameters
    start = int(request.args.get("start", type=str))-1988
    end = int(request.args.get("end", type=str))-1988

    if start > end:
        start, end = end, start

    png_1 = BytesIO()
    for n,m in dic.items():
        dic[n]=df.iloc[m].values
    plt.stackplot(x,dic.values(),labels=dic.keys())
    ax.set_title("salary distribution")
    ax.set_xlabel("Heisei")
    ax.set_ylabel("people(thousands)")
    plt.grid(True)
    ax.legend()
    ax.set_xlim([start, end])
    #plt.xticks(rotation=30)

    plt.savefig(png_1, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_1.getvalue())

    return "data:image/png:base64," + img_data


@app.route("/plot/<idNo>")
def plot_part(idNo):
    dic=dic0.copy()
    fig, ax = plt.subplots(1,1)

    # Obtain query parameters
    start = int(request.args.get("start", type=str))-1988
    end = int(request.args.get("end", type=str))-1988
    lst = request.args.get("list", type=str)
    lst=lst.split(",")
    lst2=[]
    for h in range(len(lst)):
        lst2=lst2+lst[h].split(":")
    lst2=[int(lst2[v]) for v in range(len(lst2))]
    dic_num={}
    print(lst)
    print(lst2)
    temp=[]
    #idno = request.args.get("idno", type=str)
    for xi in range(1,int(idNo)):
        for y in range(len(lst2)):
            if lst2[y]==xi:
                temp.append(lst2[y+1])
        dic_num[xi]=temp
        temp=[]
    print(dic_num)
    #print(idNo,lst,idno)

    if start > end:
        start, end = end, start

    png_1 = BytesIO()
    for n,m in dic.items():
        dic[n]=df.iloc[m].values
    dic2={}
    for p,q in dic_num.items():
        a=max(q)
        #print("a:",a)
        xx=0
        for xp in q:
            xx+=dic[xp]
            #print("xx:",xx)
            #del dic[xp]
        dic2[a]=xx
        #print(dic[a])
    #print("dic:",dic)
    for n,m in dic2.items():
        plt.plot(x,m,label=n)
    ax.set_title("salary distribution")
    ax.set_xlabel("Heisei")
    ax.set_ylabel("people(thousands)")
    plt.grid(True)
    ax.legend()
    ax.set_xlim([start, end])
    #plt.xticks(rotation=30)

    plt.savefig(png_1, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_1.getvalue())

    return "data:image/png:base64," + img_data

@app.route("/area/<idNo>")
def area_part(idNo):
    dic=dic0.copy()
    fig, ax = plt.subplots(1,1)

    # Obtain query parameters
    start = int(request.args.get("start", type=str))-1988
    end = int(request.args.get("end", type=str))-1988
    lst = request.args.get("list", type=str)
    lst=lst.split(",")
    lst2=[]
    for h in range(len(lst)):
        lst2=lst2+lst[h].split(":")
    lst2=[int(lst2[v]) for v in range(len(lst2))]
    dic_num={}
    print(lst)
    print(lst2)
    temp=[]
    #idno = request.args.get("idno", type=str)
    for xi in range(1,int(idNo)):
        for y in range(len(lst2)):
            if lst2[y]==xi:
                temp.append(lst2[y+1])
        dic_num[xi]=temp
        temp=[]
    print(dic_num)
    #print(idNo,lst,idno)

    if start > end:
        start, end = end, start

    png_1 = BytesIO()
    for n,m in dic.items():
        dic[n]=df.iloc[m].values
    dic2={}
    for p,q in dic_num.items():
        a=max(q)
        xx=0
        for xp in q:
            xx+=dic[xp]

        dic2[a]=xx

    plt.stackplot(x,dic2.values(),labels=dic2.keys())
    ax.set_title("salary distribution")
    ax.set_xlabel("Heisei")
    ax.set_ylabel("people(thousands)")
    plt.grid(True)
    ax.legend()
    ax.set_xlim([start, end])
    #plt.xticks(rotation=30)

    plt.savefig(png_1, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_1.getvalue())

    return "data:image/png:base64," + img_data


# #2枚目の図示のために少しデータをまとめる
# dic2=dic.copy()
# dic2["~200"]=dic2['~100']+dic2['~200']
# dic2["1500~"]=dic2['~2000']+dic2['~2500']+dic2['2500~']
# del dic2['~100'],dic2['~2000'],dic2['~2500'],dic2['2500~']

if __name__ == "__main__":
    app.run(debug=True, port=5000)
