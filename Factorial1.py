from flask import Flask,render_template
Factorial1=Flask(__name__)
@Factorial1.route("/",methods=["GET","POST"])
def fact1():
    num1=3
    fact1=3*2*1
    print(fact1)
    return render_template("1.html",message1=num1, message2=fact1)
if __name__=="__main__":
    Factorial1.run(debug=True)
