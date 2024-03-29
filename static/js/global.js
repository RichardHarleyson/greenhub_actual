/**
 * Created by Валентин on 29.05.2018.
 */

 // ===============================================

$(document).ready(function(){
	$('.datepicker').datepicker({
    language: 'ru'
	});
})

$(document).ready(function(){
	$('#crm_form_add_new_client').submit(function(){
		event.preventDefault();
		var data = new FormData(document.getElementById('crm_form_add_new_client'));
		$.ajax({
			url: '/global_crm/add_client',
			type: 'POST',
			data: data,
			processData: false,
			contentType: false,
			success: function(res){
				console.log(res);
			}
		})
	});
})

$(document).ready(function(){
// 	$('#bevents').html($('#content_counts').data('clients_count'));
// 	$('#bclients').html($('#content_counts').data('events_count'));
// 	$('#crm_form_add_new_client').submit(function(){
// 		event.preventDefault();
// 		var form_data = $(this).serialize();
// 		$.ajax({
// 			url: $(this).attr('action'),
// 			type: 'POST',
// 			data: form_data,
// 			success: function(res){
// 				$('#client_add_status').html('<h3>Клиент Добавлен</h3>');
// 				location.reload();
// 			}
// 		});
// 		return false;
// 	});
// 	$('#crm_form_add_new_event').submit(function(){
// 		event.preventDefault();
// 		var form_data = $(this).serialize();
// 		$.ajax({
// 			url: $(this).attr('action'),
// 			type: 'POST',
// 			data: form_data,
// 			success: function(res){
// 				$('#event_add_status').html('<h3>Событие Добавлено</h3>');
// 				location.reload();
// 			}
// 		});
// 		return false;
// 	});
	// $('.event_on').on('click', function(){
	// 	$(this).removeClass('event_on');
	// 	$(this).addClass('event_off');
	// 	$(this).removeClass('text-danger');
	// 	$(this).addClass('text-success');
	// 	$(this).html('Выполнено');
	// 	$.ajax({
	// 		url: '/gh_crm/update_event_status',
	// 		type: 'POST',
	// 		data: {event_id: $(this).data('event_id'), event_status: 'Выполнено'},
	// 		success: function(rest){
	// 		}
	// 	});
	// 	return false;
	// });
	// $('.event_off').on('click', function(){
	// 	$(this).removeClass('event_off');
	// 	$(this).addClass('event_on');
	// 	$(this).removeClass('text-success');
	// 	$(this).addClass('text-danger');
	// 	$(this).html('Не Выполнено');
	// 	$.ajax({
	// 		url: '/gh_crm/update_event_status',
	// 		type: 'POST',
	// 		data: {event_id: $(this).data('event_id'), event_status: 'Не Выполнено'},
	// 		success: function(rest){
	// 		}
	// 	});
	// 	return false;
	// });
	// $('.client_on').click(function(){
	// 	$(this).removeClass('client_on');
	// 	$(this).addClass('client_off');
	// 	$(this).removeClass('text-success');
	// 	$(this).addClass('text-secondary');
	// 	$.ajax({
	// 		url: '/gh_crm/update_client_status',
	// 		type: 'POST',
	// 		data: {client_id: $(this).data('client_id'), client_status: '0'},
	// 		success: function(rest){
	// 		}
	// 	});
	// 	return false;
	// });
	// $('.client_off').click(function(){
	// 	$(this).removeClass('client_off');
	// 	$(this).addClass('client_on');
	// 	$(this).removeClass('text-secondary');
	// 	$(this).addClass('text-success');
	// 	$.ajax({
	// 		url: '/gh_crm/update_client_status',
	// 		type: 'POST',
	// 		data: {client_id: $(this).data('client_id'), client_status: '1'},
	// 		success: function(rest){
	// 		}
	// 	});
	// 	return false;
	// });
});

function reload_crm(){
	// $('#crm_core').html('');
	$.ajax({
		url: '/gh_crm/event_page',
		type: 'GET',
		success: function(res){
			$('#crm_core').html(res);
		}
	});
}

$(document).ready(function(){
	$('.comment_textarea').focus(function () {
	    $(this).animate({ height: "10rem", width:"25rem" }, 300);
	});

	$('.comment_textarea').focusout(function () {
	    $(this).animate({ height: "2.5rem", width:"11rem" }, 300);
	});
})

$(document).ready(function(){
	$('.client_tform').submit(function(){
		event.preventDefault();
		$(this).parent().find('textarea').blur();
		var felem = document.getElementById('client_tform_'+$(this).data('client_id'));
		var data = new FormData(felem);
		data.append('client_id', $(this).data('client_id'));
		$.ajax({
			type: 'POST',
			url: '/global_crm/upd_client',
			data: data,
			processData: false,
			contentType: false,
			success: function(res){
				// console.log(res);
				// alert(res);
				// $(this).parent().css('background', 'green');
				// setTimeout(function(){
				// 	$(this).parent().css('background', 'white');
				// }, 2000);
				document.location.reload();
			}
		})
	});
});

$(document).ready(function(){
 $('#crm_form_add_new_vehicle').submit(function(){
	 event.preventDefault();
	 console.log('pressed');
	 var data = new FormData(document.getElementById('crm_form_add_new_vehicle'));
	 $.ajax({
		 type: ' POST',
		 url: '/global_crm/add_vehicle',
		 // data: data,
		 processData: false,
		 contentType: false,
		 success: function(res){
			 console.log('Result: ');
			 console.log(res);
		 },
		 fail: function(res){
			 console.log('Failed');
		 }
	 })
 });
});

function del_client(elem){
	// console.log("#2 initiated");
	event.preventDefault();
	$.ajax({
		type: 'POST',
		url: '/global_crm/del_client',
		data: {client_id: $(elem).data('client_id')},
		success: function(res){
			console.log(res);
			$('#client_tform_'+$(elem).data('client_id')).parent().css('background', 'red');
			setTimeout(function(){
				$('#client_tform_'+$(elem).data('client_id')).parent().hide();
			}, 2000);
		}
	})
}

function call_comment_modal(elem){
	$('#modal_comment_textarea').val($(elem).data('client_comment'));
	$('#modal_comments').modal('show');
}

function upd_event(element){
	$('#create_modal').modal();
	$('#crm_form_add_new_event').attr('action','/gh_crm/update_event');
	$('form select[name=client_id] option[value="'+$(element).data('event_client')+'"]').attr('selected', 'selected');
	$('form select[name=event_curator] option[value="'+$(element).data('event_curator')+'"]').attr('selected', 'selected');
	$('form select[name=event_type] option[value="'+$(element).data('event_type')+'"]').attr('selected', 'selected');
	$('form input[name=event_date]').val($(element).data('event_date'));
	$('form textarea[name=comment]').val($(element).data('event_comment'));
	$('form input[name=event_id]').val($(element).data('event_id'));
}

function upd_client(element){
	$('#add_new_client_modal').modal();
	$('#crm_form_add_new_client').attr('action','/gh_crm/update_client');
	$('form input[name=client_name]').val($(element).data('client_name'));
	$('form input[name=client_id]').val($(element).data('client_id'));
	$('form select[name=client_type] option[value="'+$(element).data('client_type')+'"]').attr('selected', 'selected');
	$('form input[name=veh_body]').val($(element).data('veh_body'));
	$('form input[name=veh_budget]').val($(element).data('veh_budget'));
	$('form input[name=client_phone]').val($(element).data('client_phone'));
	$('form input[name=client_email]').val($(element).data('client_email'));
	$('form textarea[name=comment]').val($(element).data('client_comment'));
}

function remove_client(element){
	if(confirm('Удалить?')){
		$.ajax({
			url: '/gh_crm/remove_client',
			type: 'POST',
			data: {client_id : $(element).data('client_id')},
			success: function(res){
				$('tr[data-client_id='+$(element).data('client_id')+']').addClass('bg-danger');
			}
		})
	}
}

function remove_event(element){
	if(confirm('Удалить?')){
		$.ajax({
			url: '/gh_crm/remove_event',
			type: 'POST',
			data: {event_id : $(element).data('event_id')},
			success: function(res){
				$('tr[data-event_id='+$(element).data('event_id')+']').addClass('bg-danger');
			}
		})
	}
}

$(document).ready(function(){
		$('.file_input').change(function(){
			// alert('Smth changed');
			var curr_form = document.getElementById($(this).data('form_type'));
			var formdata = new FormData(curr_form);
			formdata.append('client_id', $(this).data('client_id'));
			formdata.append('file_type', $(this).data('file_type'));
			for (var pair of formdata.entries()) {
			    console.log(pair[0]+ ', ' + pair[1]);
			}
			$.ajax({
				url: '/global_crm/upload_client_file',
				type: 'POST',
				data: formdata,
				processData: false,
				contentType: false,
				success: function(res){
					console.log(res);
					alert(res);
					// $(this).parent().find('.btn_file_input').css('background-color', 'green');
					// setTimeout(function(){$(this).parent().find('.btn_file_input').css('background-color', '#007bff')});
				}
			});
		});
})

// Добавить Авто

$(document).ready(function(){
	$('#add_veh_send').submit(function(){
		event.preventDefault();
		var data = new FormData($('form')[0]);
		$.ajax({
			url: '/electrocars/add_veh_send',
			type: 'POST',
			data: data,
			processData: false,
			contentType: false,
			success: function(res){
				$('#add_veh_send').trigger('reset');
				$('#add_veh_status').html('<h3>Успешно Добавлено</h3>');
				setTimeout(function(){$('#add_veh_status').html('');}, 2000);
			}
		});
	});
});

$(document).ready(function(){
	var items = $('.check_file_status').each(function(){
		// console.log($(this).data('client_files'));
		if($(this).data('client_files') != ''){
			$(this).parent().find('.file_status').html('<i class="fas fa-check fa-2x text-success align-middle mx-2"></i>');
		}else {
			$(this).parent().find('.file_status').html('<i class="fas fa-times fa-2x text-danger align-middle mx-2"></i>');
		}
	});
});

function call_imgmodal(elem){
	var veh_photo = $(elem).data('veh_photo');
	$('#veh_photo_to_set').prop('src', veh_photo);
}

function call_imgmodal_client(elem){
	var files = $(elem).data('client_files');
	var files_id = $(elem).data('files_id');
	var split_files = files.split(";");
	var split_files_id = files_id.split(";");
	$('#imgmodal_inside').html('');
	var fhtml = '';
	for(let i = 0; i < (split_files.length - 1); i++){
		fhtml += '<img class="del_file" data-file_id="'+split_files_id[i]+'" src="'+split_files[i]+'" alt="" style="width:100%" >'
	}
	try{
		$('#imgmodal_inside').slick('unslick');
	}catch{
		console.log('unslick failed');
	}
	$('#imgmodal_inside').html(fhtml);
	try{
		$('#imgmodal_inside').slick({
			infinite: true,
			slidesToShow: 1,
			slidesToScroll: 1,
			prevArrow: "#imgmodal_prev",
			nextArrow: "#imgmodal_next",
		})
		$('#imgmodal_inside').slick('setPosition');
	}catch{
		console.log('Some error happened');
	}
}

function file_del(elem){
	var item_id = $('.slick-current').data('file_id');
	var data = new FormData();
	data.append('file_id', item_id);
	$.ajax({
		url: '/global_crm/del_client_file',
		type: 'POST',
		data: data,
		processData: false,
		contentType: false,
		success: function(rest){
			console.log(rest);
			$(elem).css('background', 'red');
			setTimeout(function(){ $(elem).css('background', 'white')}, 2000);
		}
	})
}

$(document).ready(function(){
	$('#modalIMG').on('shown.bs.modal', function () {
		$('#imgmodal_inside').slick('setPosition');
	})
})

// Update авто
function upd_veh(elem){
		event.preventDefault();
		var gparent = $(elem).parent().parent();
		console.log($('#file_'+$(elem).data('veh_id'))[0].files[0]);
		var data = new FormData();
		data.append('veh_id', $(elem).data('veh_id'));
		data.append('veh_model', gparent.find('input[name="veh_model"]').val());
		data.append('veh_year', gparent.find('input[name="veh_year"]').val());
		data.append('veh_mileage', gparent.find('input[name="veh_mileage"]').val());
		data.append('veh_color', gparent.find('input[name="veh_color"]').val());
		data.append('veh_color_in', gparent.find('input[name="veh_color_in"]').val());
		data.append('veh_price', gparent.find('input[name="veh_price"]').val());
		data.append('veh_type', gparent.find('input[name="veh_type"]').val());
		data.append('veh_status', gparent.find('input[name="veh_status"]').val());
		data.append('veh_incomming_date', gparent.find('input[name="veh_incomming_date"]').val());
		data.append('veh_photo', $('#file_'+$(elem).data('veh_id'))[0].files[0]);
		$.ajax({
			url: '/electrocars/upd_veh',
			type: 'POST',
			data: data,
			processData: false,
			contentType: false,
			success: function(rest){
				gparent.css('background', 'green');
				setTimeout(function(){gparent.css('background', 'white')}, 2000);
			}
		})
	}

function del_veh(elem){
	if(confirm('Уверены?') == false){
		return 0;
	}
	event.preventDefault();
	var gparent = $(elem).parent().parent();
	var data = new FormData();
	data.append('veh_id', $(elem).data('veh_id'));
	$.ajax({
		url: '/electrocars/del_veh',
		type: 'POST',
		data: data,
		processData: false,
		contentType: false,
		success: function(rest){
			gparent.css('background', 'red');
			setTimeout(function(){ gparent.removeClass('d-flex');gparent.hide()}, 2000);
		}
	});
}

// Тоглеры управления авто
$(document).ready(function(){
	$('#add_veh_collapse').on('show.bs.collapse', function(){
		$('#ctrl_veh_collapse').collapse('hide');
	});
	$('#ctrl_veh_collapse').on('show.bs.collapse', function(){
		$('#add_veh_collapse').collapse('hide');
	});
})

$(document).ready(function(){
	$("#pop").on("click", function(e) {
   // e.preventDefault();
   $('#the-modal').modal('toggle');
	});
	// $('#the-modal').on("click", function(e) {
	// 	$("body").find(".modal").removeClass("visible");
	// });
})



 // ===============================================

//timeline

//$(".timeline-panel").hide(0);

$("i").click(function() {
	    $('.timeline-panel').show(0);
});

$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip()
})
// ==============================================

$(document).ready(function(){
	Array.prototype.forEach.call(document.querySelectorAll('.pd-parallax'), function(elem){
		elem.style.backgroundImage='url('+elem.getAttribute('data-bg-image')+')';
	});
});

//Aux_client
$(document).ready(function(){
	$('#aux_client_form').submit(function(){
		event.preventDefault();
		var form_data = $(this).serialize();
		$.ajax({
			url : $(this).attr('action'),
			type: 'POST',
			data: form_data,
			success: function(res){
				$('form[id=aux_client_form]').trigger('reset');
				// alert(form_data);
				$('.message_status').html('<h5>Менеджер подберет авто и свяжется с вами</h5>');
			},
		});
	});
});

// Модальное окно записи на тест драйв
$(document).ready(function(){
		$("#f1_test_drive").submit(function(){
			var form_data = $(this).serialize();
			$.ajax({
				url: $(this).attr('action'),
				type: "POST",
				data: form_data,
				success: function(data) {
					$('form[id=f1_test_drive]').trigger('reset');
					tdfa();
				},
				// error: function(){ ... }
			});
			return false
		});
});

function tdfa(){
    $( "#tdfa" ).removeClass( "hidden" );
}

// Модальное окно записи для звонка
$(document).ready(function(){
    $("#call-me-form").submit(function() { //устанавливаем событие отправки для формы с id=form
        var form_data = $(this).serialize(); //собераем все данные из формы
        $.ajax({
            url: $(this).attr('action'), //путь до php фаила отправителя
            type: "POST",
            data: form_data,
            success: function() {
                $('form[id=call-me-form]').trigger('reset');
                cma();
            },
						// error: function(){ ... }
        });
        return false;
    });
});

function cma(){
    $( "#cma" ).removeClass( "hidden" );
}

// Человек хочет машину
$(document).ready(function(){
    $('.iwantcarform').submit(function (){
        var form_data = $(this).serialize(); //собераем все данные из формы
        $.ajax({
            url: $(this).attr('action'), //путь до php фаила отправителя
            type: "POST", //Метод отправки
            data: form_data,
            success: function(data) {
                $('form[class=iwantcarform]').trigger('reset');
                iwa();
            }
        });
        return false;
    });
});

function iwa(){
    $("#iwa" ).removeClass( "hidden" );
}

//Убираем все со страницы
$(document).ready(function(){
    $('.clear_page').css({'cursor': 'pointer'});
    $('.clear_page').on('click', function(){
        $('#vehicle_global').empty();
        if($(this).attr("id") == 'show_fine_vehs' || $(this).attr("id") == 'show_available'){
            var data = {todo: 'available', veh_state: 'fine'};
            $.ajax({url: "https://greenhub.pro/veh_todo.php", type: "POST", data: data}).done(function( html ) {
                $("#vehicle_global").append(html);
                $('.hit').hide();
                $('.carousel').carousel('pause');
            });
        }
		if($(this).attr("id") == 'show_salon'){
            var data = {todo: 'salon'};
            $.ajax({url:"https://greenhub.pro/veh_todo.php", type: "POST", data: data}).done(function(html){
                $("#vehicle_global").append(html);
                $('.carousel').carousel('pause');
            });
        }
        if($(this).attr("id") == 'show_comming'){
            var data = {todo: 'comming'};
            $.ajax({url:"https://greenhub.pro/veh_todo.php", type: "POST", data: data}).done(function(html){
                $("#vehicle_global").append(html);
                $('.carousel').carousel('pause');
            });
        }
        if($(this).attr("id") == 'show_comming'){
            var data = {todo: 'comming'};
            $.ajax({url:"https://greenhub.pro/veh_todo.php", type: "POST", data: data}).done(function(html){
                $("#vehicle_global").append(html);
                $('.carousel').carousel('pause');
            });
        }
    });
});

$(document).ready(function(){
    $('#load_photo_btn').on('click', function(){
        $('#vehicle_block').empty();
        $.ajax({
            url:"https://greenhub.pro/tmp/cms/cms_todo.php",
            type:"POST",
            data: {todo: 'load_photos'},
            success: function(res){
                $('#vehicle_block').append(res);
            }
        });
    });
});

$(document).on('click','.set-photo',function(){
    var veh_data = {veh_id: $(this).attr('data-vehicle-id'), photo_id: $(this).attr('data-photo-id')};
    $.ajax({
        url:"https://greenhub.pro/tmp/cms/cms_set_photo.php",
        type:"POST",
        data:veh_data,
        success:function(res){
            // alert(res);
            $(res).empty();
            var html = "<h4>Фото установлено</h4>";
            $(res).append(html);
        }
    });
});
// lot_form
$(document).ready(function(){
	$("form.lot_form :input").change(function(){
		var item = $(this).parent().find('label');
		lot_total_price(this, $(this).data('min'), $(this).data('max'), item);
	});
});

function lot_total_price(price, min, max, label){
	label.html("<h5>Всего: <span class='text-success'>"+(Number($(price).val()) + Number(min))+"$ - "+(Number($(price).val()) + Number(max))+"$</span></h5>")
}
