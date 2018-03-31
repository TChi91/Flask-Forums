/*DELETE*/
$(function ()
    {
        $(".del").click(function(event)
        {
            var id = event.target.id;
            $.ajax({
                type: "DELETE",
                url: "/api/topic/delete/"+id,
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (response)
                {
                   alert("Delete topic successfully !");
                   location.reload();
                }
            });
        });
    });