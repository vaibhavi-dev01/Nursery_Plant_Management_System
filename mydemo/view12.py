 '''dict2={'e1':'' }
    if(request.method == 'POST'):
        us=request.POST['name']
        pas=request.POST['pass']
        s1=plant.objects.filter(nm=us,ps=pas).exists()
        if(s1 and us=='Admin'):
            return HttpResponseRedirect('/adminhome')
        elif(s1):
            return HttpResponseRedirect('/userhome')
        else:
            dict2={'e1':'Invalid Login'}
            return render('login.html',dict2)
    return render(request,'login.html')
'''

'''<html>
    <head>
        <title>MY web Page</title>
        <style>
            #big{
                width:500px;
                height:500px;
                border:2px solid black;
                margin-left:400px;
                margin-top:50px;
                border-radius:20%;
                background-color:white;
                box-shadow:7px 7px 2px black;
            }
            #ad{
                width:300px;
                height:100px;
                margin-left:100px;
                margin-top:-60px;
                border-radius:10px;
            }
            #loadedImage {
            display: none;
            border-radius: 10px;
            width:10px;
            height:570px;
           margin-top:-500px;
           margin-left:-300px;
        }
        </style>
            <script src="jquery.js"></script>
    
</head>
<body bgcolor="lightgray">
    <div id="big">
        <h1 align="center">🙏</h1>
        <h1 align="center" style="margin-top:40px;font-size:50px;">Thank You!</h1>
        <h3 style="margin-left:70px;">A Confirmation as been sent to your email.<br>
            Since you're here , join our list for discounts!<br></h3>
            <form action=" " method="post">
                <h3 style="margin-left:20px; margin-top:50px;">Address:</h3><input type="text" id="ad"><br>
                <button type="button" id="b1" style="margin-left:220px; margin-top:30px; padding:10px;border-radius:20%;">Confirm</button>
            </form>
            <img id="loadedImage" src="/static/order.webp" >
    </div>
   <script>
        $(document).ready(function(){
            $('#b1').click(function(){
                $('#loadedImage').fadeIn(2000); // Fade in over 2 seconds
            });
        });
    </script>
</body>
</html>'''