window.onload = () => {
    // $('#type_course_update').click();
    $('.update_type_course_ajax').on('click', 'button[type="button"]', (e) => {
        let t_href = e.target.value;
        $.ajax({
            url: '/type-course-list/',
            type: 'POST',
            data: jQuery.param({id: t_href, method: 'detail'}),
            success: function (response) {
                console.log(response);
                $('.update_type').html(response)
                $('#type_course_update_id').trigger('click');

            },
           error: function(error){
				console.log(error);
			}
        });
        e.preventDefault();
    })

}


