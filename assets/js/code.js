document.getElementById("set_basket").addEventListener("click",function(){

    $.ajax({
        url : "/basket",
        type : "POST",
        data : {
            "id" : document.getElementById("productid").value
        },
        success : function(res){
            iziToast.success({
                message: res.text,
                position: 'bottomRight',
                timeout: 2000,
            });
        },
        error : function(res){
            iziToast.error({
                message: data.message,
                position: 'bottomRight',
                timeout: 3000,
            });
        }
    })

});