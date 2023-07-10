from flask import Flask,jsonify,request
app=Flask(__name__)
posts=[]
count=1
# post method
app.route("/post",method=['POST'])
def post():
    global count
    data=request.get_json()
    name=data.get('name')
    caption=data.get('caption')
    if not name or not caption:
        return jsonify({'error':'fill required detials'}),404
    post={
        'id':count,
        'name':name,
        'caption':caption,
        'likes':0,
        'comments':[]
    }
    posts.append(post)
    count+=1
# get method
@app.route("/",method=['GET'])
def get():
    return jsonify({'posts':posts})
# delete method
@app.route('/delete/<int:post_id>',method=["DELETE"])
def delete(post_id):
    global posts
    post=next(x for x in posts if x[id]==post_id)
    if not post:
        return jsonify({'error':'post not found'}),404
    posts=[x for x in posts if x[id]!=post_id]
    return jsonify({"message":"post deleted"})
if__name__=='main':
    app.run(port=8080)