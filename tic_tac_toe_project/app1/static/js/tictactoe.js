$(document).ready( function(){
    $(document).on('keyup' , '.check_availiblity', function (){
        var check = $(this).val()
        
        console.log(check)
        if(check !== null){
            $.ajax({
                url: 'check_name',
                method: 'POST',
                data: {
                    check ,
                },
                success: function (data) {
                    console.log('working')
                    console.log(data)
                }
            })
        }
    })
})