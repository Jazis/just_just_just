$(function() {
	$(document).on('click', '.e-helper-action', stepHandler);

	var msg;

	function stepHandler (event) {
		var action = $(this).data('action');

		if (msg) {
			msg.remove();
		};

		switch (action) {
			case 'show-welcome':
				msg = show_welcome($('#helper'));
				break;
			case 'need-help':
				msg = step_is_regestered($('#helper'));
				break;
			case 'need-help-twice':
				msg = step_is_regestered_twice($('#helper'));
				break;
			case 'has-account':
				msg = step_is_login($('#login-button'));
				break;
			case 'has-not-account':
				msg = step_go_register($('#register-info'));
				break;
			case 'step-login-accept':
				break;
			case 'step-login-cancel':
				msg = step_enter_login($('#login-form'));
				break;
			case 'step-forget-mail-register':
				msg = step_forget_mail_register($('#remember-password'));
				break;
			case 'step-forget-mail-address':
				msg = step_forget_mail_address($('#login-form'));
				break;
			case 'step-register-help-secret-cancel':
				msg = step_register_help_secret_cancel($('#register-info'));
				break;
			case 'step-register-help-data-cancel':
				msg = step_register_help_data_cancel($('#register-info'));
				break;
            case 'step-lack-data-msg':
                msg = step_lack_data_msg($('#register-info'));
                break;
            case 'cancellation-registration':
                msg = cancellation_registration($('#register-info'));
                break;
			case 'step-no-access':
				msg = step_no_access($('.relative-position-for-help'));
				break;
			case 'step-already-registered':
				msg = step_already_registered($('.relative-position-for-help'));
				break;
			case 'step-not-registered':
				msg = step_not_registered($('.relative-position-for-help'));
				break;
			case 'step-reg-user-confirmed':
				msg = step_reg_user_confirmed($('.relative-position-for-help'));
				break;
			case 'step-reg-user-exists':
				msg = step_reg_user_exists($('.relative-position-for-help'));
				break;
			case 'step-reg-user-exists-twice':
				msg = step_reg_user_exists_twice($('.relative-position-for-help'));
				break;
		};

		return false;
	};

    /*********------Help window--------************/
	function print_step_help(config) {
		var option = $.extend(true, {title: '', message: '', buttons: '', arrow: ''}, config);
		var popover = '<div role="alert" class="b-helper-msg alert alert-warning text-left' + option.arrow + '">'+
			'<div class = "panel"><button type="button" data-dismiss="alert" aria-label="Close" class="close" title="Закрыть"><span aria-hidden="true"></span></button></div>'+
			(option.title ? '<div class="b-helper-msg__title">' + option.title + '</div>' : '') +
			(option.message ? '<div class="b-helper-msg__text">' + option.message + '</div>' : '') +
			(option.buttons ? '<div class="b-helper-msg__button"><div>' + option.buttons + '</div></div>' : '') +
			'</div>';

		return $(popover);
	};
    function template_for_other_page(config) {
        var option = $.extend(true, {title: '', message: '', buttons: '', arrow: ''}, config);
        var popover = '<div role="alert" class="b-helper-msg alert alert-warning text-left cancellation-of-registration  b-helper-msg-for-form' + option.arrow + '">'+
            '<div class = "panel"><button type="button" data-dismiss="alert" aria-label="Close" class="close" title="Закрыть"><span aria-hidden="true"></span></button></div>'+
            (option.title ? '<div class="b-helper-msg__title">' + option.title + '</div>' : '') +
            (option.message ? '<div class="b-helper-msg__text">' + option.message + '</div>' : '') +
            (option.buttons ? '<div class="b-helper-msg__button"><div>' + option.buttons + '</div></div>' : '') +
            '</div>';

        return $(popover);
    };

    /*********------п.1 --------************/
    function show_welcome () {

        var html = print_step_help({
            message: '<p class="txt-align-c">У Вас возникли трудности при осуществлении входа в «Личный кабинет»?</p>',
            buttons:
            '<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="need-help-twice">Зарегистрированный пользователь</a>' +
            '<a class="btn btn-danger btn-xs m_l1 m_r1" href="/users/loginWithoutReg">Незарегистрированный пользователь</a>'
        });
        $('#helper').append(html);
        return html;
    };
    /*********------п.2 --------************/
	function step_is_regestered () {
		var html = print_step_help({
			title: '<p class="txt-align-c">Неверный логин или пароль.</p><p class="txt-align-c">Проверьте введенные данные и повторите попытку.</p>'
		});
		$('#helper').append(html);

		return html;
	};
	function step_is_regestered_twice () {
		var html = print_step_help({
			message: '<p class="txt-align-c" style="font-size:18px;">Вы забыли (утеряли):</p>',
			buttons:
			'<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="has-account">Пароль</a>' +
			'<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="step-login-cancel">Логин</a>' +
			'<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="step-register-help-data-cancel">Логин и пароль, утерян доступ</br>к электронной почте, на которую</br>производилась регистрация</a>'});
		$('#helper').append(html);

		return html;
	};
    /*********------п.2.1 --------************/
	function step_is_login (element) {
		var html = print_step_help({
            arrow: ' t-bottom-arrow',
			message: '<p class="txt-align-c" style="font-size:18px;">Воспользуйтесь мастером по восстановлению пароля </br> </br><strong><a class="txt-align-c btn-help-form e-no-link" href="/users/resetPassword" role="button" data-action="step-register-help-data-cancel">Восстановить пароль</a></strong></p>'

		});
		$('#remember-password').append(html);
        $('.b-helper-msg .panel button.close').after('<a class="back-to-previous-help e-helper-action m_l1 m_r1" href="#" role="button" data-action="need-help-twice" title="Назад"><span aria-hidden="true"></span></a>');
		return html;
	};
    /*********------п.2.4-------************/
	function step_enter_login (element) {
		var html = print_step_help({
			title: '<p>Логином для входа в «Личный кабинет» является Ваш табельный номер.</p>',
			message:
			'<p><b>Узнать его можно следующим образом:</b></p>' +
            '<ol> ' +
                '<li>Логин содержится в письме, ранее направленном на адрес электронной почты, указанной Вами при регистрации в «Личном кабинете»;</li>' +
				'<li>Вы можете воспользоваться мастером по восстановлению пароля, при этом на адрес электронной почты, указанной Вами при регистрации в «Личном кабинете», поступит письмо с Вашим логином и ссылкой для восстановления пароля.</li>' +
				'<li>В расчетном листке в поле «Таб№»;</li>' +
				'<li>Обратиться в кадровый орган, ответственный за ввод информации в единую базу данных по Вашей воинской части, ФРП (финансово-расчетный пункт) управления финансового обеспечения, в котором Ваша воинская часть состоит на финансовом обеспечении.</li>' +
            '</ol>',
			buttons:
				'<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="has-not-account">Не удалось узнать логин ни</br>  одним из способов</a>'
		});
		$('#helper').append(html);
        $('.b-helper-msg .panel button.close').after('<a class="back-to-previous-help e-helper-action m_l1 m_r1" href="#" role="button" data-action="need-help-twice" title="Назад"><span aria-hidden="true"></span></a>');
		return html;
	};
    /*********------ п.2.2-------************/
	function step_go_register (element) {
		var html = print_step_help({
			message: '<p>Вам следует пройти процедуру отмены регистрации. Для отмены регистрации в «Личном кабинете» необходимо направить заявление на имя руководителя Единого расчетного центра Министерства обороны Российской Федерации (по адресу: 105066, г. Москва, ул. Спартаковская, д. 2Б или адресу электронной почты: <a href="mailto:erc@mil.ru" style="color:#ae1d12;">erc@mil.ru</a>) <span style="font-weight: bold;text-decoration: underline;">с приложением рапорта, подписанного командиром воинской части, и заверенного гербовой печатью</span>. В рапорте необходимо указать фамилию, имя, отчество, дату рождения, личный номер военнослужащего (для гражданского персонала – СНИЛС), наименование воинской части (организации), контактного номера телефона, а также изложить суть проблемы по отмене регистрации в «Личном кабинете».</p>'
		});
		$('#helper').append(html);
		$('#helper .b-helper-msg').css("width","425px");
        $('.b-helper-msg .panel button.close').after('<a class="back-to-previous-help e-helper-action m_l1 m_r1" href="#" role="button" data-action="step-login-cancel" title="Назад"><span aria-hidden="true"></span></a>');
		return html;
	};


	function step_register_help_secret_cancel (element) {
		var html = print_step_help({
			arrow: ' t-bottom-arrow',
			message:
				'<p>Вам необходимо позвонить на горячую линию ФКУ «ЕРЦ МО РФ» по бесплатному номеру телефона 8-800-737-7-737 и уточнить правильность введения Ваших персональных данных в единую базу данных.</p>' +
				'<p><strong>Персональные данные в единой базе данных соответствуют?</strong></p>',
			buttons:
				'<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="step-register-help-data-cancel">Нет</a>' +
				'<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="has-not-account">Да</a>'
		});
		$('#page').append(html);

		return html;
	};
    /*********------п.2.3.1 --------************/
	function step_register_help_data_cancel (element) {
        var html = print_step_help({
            message: '<p>Вам следует пройти процедуру отмены регистрации. Для отмены регистрации в «Личном кабинете» необходимо направить заявление на имя руководителя Единого расчетного центра Министерства обороны Российской Федерации (по адресу: 105066, г. Москва, ул. Спартаковская, д. 2Б или адресу электронной почты: <a href="mailto:erc@mil.ru" style="color:#ae1d12;">erc@mil.ru</a>) <span style="font-weight: bold;text-decoration: underline;">с приложением рапорта, подписанного командиром воинской части, и заверенного гербовой печатью</span>. В рапорте необходимо указать фамилию, имя, отчество, дату рождения, личный номер военнослужащего (для гражданского персонала – СНИЛС), наименование воинской части (организации), контактного номера телефона, а также изложить суть проблемы по отмене регистрации в «Личном кабинете».</p>'

        });
        $('#helper').append(html);
		$('#helper .b-helper-msg').css("width","425px");
        $('.b-helper-msg .panel button.close').after('<a class="back-to-previous-help e-helper-action m_l1 m_r1" href="#" role="button" data-action="need-help-twice" title="Назад"><span aria-hidden="true"></span></a>');

        return html;
	};

	/*********------ п.2.5-------************/
	function step_not_registered(container) {
		var html = template_for_other_page({
			title: 'По введенным данным регистрация не производилась',
			message:
			'<p>Проверьте введенные данные, повторите попытку ввода данных для восстановления пароля.</p>' +
			'<p>Для уточнения правильности Ваших данных обратитесь в кадровый орган, ответственный за ввод информации в единую базу данных по Вашей воинской части, ФРП (финансово-расчетный пункт) управления финансового обеспечения, в котором Ваша воинская часть состоит на финансовом обеспечении или позвоните на горячую линию ФКУ «ЕРЦ МО РФ» 8-800-737-7-737.</p>' +
			'<p>Если ранее Вы не осуществляли регистрацию в «Личном кабинете», воспользуйтесь функцией <a class="help-link" href="/users/reg">Пройти регистрацию</a>.</p>' +
			'<p>После осуществления регистрации вход в «Личный кабинет» будет возможен с помощью созданного Вами уникального пароля, что обеспечит сохранность личных данных и защиту от третьих лиц.</p>'
		});
		container.prepend(html);

		return html;
	};

	/*********------ п.3.2-------************/
	function step_no_access(container) {
		var html = template_for_other_page({
			title: '<div style="text-align:center;">Доступ к сведениям о размере<br> своего денежного довольствия<br> (заработной платы) в «Личном<br> кабинете» отсутствует если Вы:</div>',
			message:
			'<ol>' +
			'<li>Не состоите на денежном довольствии в ФКУ «ЕРЦ МО РФ» (для уточнения данной информации Вам необходимо обратиться к командиру воинской части, в которой Вы проходите службу (работаете))</li>' +
			'<li>Проходите службу в воинских частях, которым присвоена высокая степень секретности.  (для получения расчетных листков необходимо обратиться к командиру воинской части).</li>' +
			'<li>Не получали денежное довольствие (заработную плату) через ФКУ «ЕРЦ МО РФ» (в том случае, если Вы недавно поступили на военную службу (работу)).</li>' +
			'</ol>' +
			'<p>Если вход в «Личный кабинет» не осуществляется, проверьте еще раз введенные данные, повторите попытку ввода персональных данных. Для уточнения правильности Ваших персональных данных обратитесь в кадровый орган, ответственный за ввод информации в единую базу данных по Вашей воинской части, ФРП (финансово-расчетный пункт) управления финансового обеспечения в котором Ваша воинская часть состоит на финансовом обеспечении  или позвоните на горячую линию ФКУ «ЕРЦ МО РФ».</p>'
		});
		container.append(html);

		return html;
	};

	/*********------ п.3.4-------************/
	function step_already_registered(container) {
		var html = template_for_other_page({
			message:
			'<ul class = "dashed-mark">' +
				'<li> - Вам необходимо перейти на главную страницу и ввести Ваш логин и пароль, указанный при регистрации.</li>' +
				'<li> - Если ранее регистрацию в «Личном кабинете» Вы не проходили, следует' +
					' <a class="btn-help-form e-no-link e-helper-action" href="#" role="button" data-action="cancellation-registration">пройти процедуру отмены регистрации.</a>' +
			    '</li>' +
			'</ul>'
		});
		container.append(html);

		return html;
	};

	function step_forget_mail_register (element) {
		var html = print_step_help({
			arrow: ' t-bottom-arrow',
			message: '<p>Ранее не регистрировался в личном кабинете военнослужащего, при попытке осуществить вход выдает ошибку: «Вы уже зарегистрированы в системе. Войдите как зарегистрированный пользователь»</p>',
			buttons:
				'<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="step-login-cancel">Нет</a>' +
				'<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="step-forget-mail-address">Да</a>'
		});
		$('#page').append(html);
		return html;
	};

	function step_forget_mail_address (element) {
		var html = print_step_help({
			title: 'Вам необходимо отменить регистрацию в «Личном кабинете».',
			message: '<p>Для этого необходимо написать рапорт, заверить его у командира воинской части (руководителя организации) гербовой печатью и направить на имя руководителя ФКУ «ЕРЦ МО РФ» по адресу 105066, Москва, ул.Спартаковская, д. 2б или адресу электронной почты <a href="mailto:erc@mil.ru">erc@mil.ru</a>. В рапорте необходимо указать дату рождения, личный номер (СНИЛС), а также изложить суть проблемы.</p>',
            buttons: '<a class="btn btn-danger btn-xs e-helper-action m_l1 m_r1" href="#" role="button" data-action="step-login-cancel">Нет</a>'
		});

		$('#page').append(html);
		return html;
	};


	function step_lack_data_msg (element) {
        var html = template_for_other_page({
            message:
            '<ul class = "dashed-mark">'+
                '<li> - Вам необходимо перейти на главную страницу и ввести Ваш логин и пароль, указанный при регистрации.</li>'+
                '<li> - Если ранее регистрацию в «Личном кабинете» Вы не проходили, следует <a class="btn-help-form e-no-link e-helper-action" href="#" role="button" data-action="cancellation-registration"> пройти процедуру отмены регистрации.</a></li>'+
            '</ul>',
        });
        $('.relative-position-for-help').append(html);
        return html;
    };

    function cancellation_registration (element) {
        var html = template_for_other_page({
            message:
				'<p>Вам следует пройти процедуру отмены регистрации. Для отмены регистрации в «Личном кабинете» необходимо направить заявление на имя руководителя Единого расчетного центра Министерства обороны Российской Федерации (по адресу: 105066, г. Москва, ул. Спартаковская, д. 2Б или адресу электронной почты: <a href="mailto:erc@mil.ru" style="color:#ae1d12;">erc@mil.ru</a>) <span style="font-weight: bold;text-decoration: underline;">с приложением рапорта, подписанного командиром воинской части, и заверенного гербовой печатью</span>. В рапорте необходимо указать фамилию, имя, отчество, дату рождения, личный номер военнослужащего (для гражданского персонала – СНИЛС), наименование воинской части (организации), контактного номера телефона, а также изложить суть проблемы по отмене регистрации в «Личном кабинете».</p>'
        });
        $('.b-helper-msg').remove();
        $('.relative-position-for-help').append(html);
        $('.b-helper-msg .panel button.close').after('<a class="back-to-previous-help e-helper-action m_l1 m_r1" href="#" role="button" data-action="step-lack-data-msg" title="Назад"><span aria-hidden="true"></span></a>');
        return html;
    };

	/*********------ /users/reg -------************/
	function step_reg_user_confirmed(container) {
		var html = template_for_other_page({
			title: 'По введенным данным регистрация произведена ранее. Вход возможен только с помощью логина и пароля',
			message:
			'Перейдите на <a href="/" style="color:#ae1d12;">главную страницу ввода логина и пароля</a> либо пройдите процедуру <span style="color:#ae1d12;border-bottom:1px dashed;cursor: pointer;" onclick="toggleDescription();">отмены регистрации</span>.' +
			'<p id="cancel-reg-description" style="display:none;"> Для отмены регистрации в «Личном кабинете» необходимо направить заявление на имя руководителя Единого расчетного центра Министерства обороны Российской Федерации (по адресу: 105066, г. Москва, ул. Спартаковская, д. 2Б или адресу электронной почты: <a href="mailto:erc@mil.ru" style="color:#ae1d12;">erc@mil.ru</a>) <span style="font-weight:bold;text-decoration:underline;">с приложением рапорта, подписанного командиром воинской части, и заверенного гербовой печатью</span>. В рапорте необходимо указать фамилию, имя, отчество, дату рождения, личный номер военнослужащего (для гражданского персонала – СНИЛС), наименование воинской части (организации), контактного номера телефона, а также изложить суть проблемы по отмене регистрации в «Личном кабинете».</p>' +
			'<script type="text/javascript">' +
				'function toggleDescription(){' +
					'$("#cancel-reg-description").toggle();' +
			    '}' +
			'</script>'
		});
		container.prepend(html);

		return html;
	};

	/*********------ /users/reg -------************/
	function step_reg_user_exists(container) {
		var html = template_for_other_page({
			title: '<p class="txt-align-c">Проверьте введенные данные и повторите попытку ввода данных для регистрации.</p>'
		});
		container.prepend(html);

		return html;
	};

	function step_reg_user_exists_twice(container) {
		var html = template_for_other_page({
			title: 'Отсутствует информация в соответствии с введенными данными',
			message:
			'<p><b>Доступ к сведениям о размере своего денежного довольствия (заработной платы) в «Личном кабинете» отсутствует если:</b></p>' +
			'<ol>' +
				'<li>Вы не состоите на денежном довольствии в ФКУ «ЕРЦ МО РФ» (для уточнения данной информации Вам необходимо обратиться к командиру воинской части, в которой Вы проходите службу (работаете)).</li>' +
				'<li>Выгрузка информации по расчетным листкам по воинской части, в который Вы проходите службу, не производится (для получения расчетных листков необходимо обратиться к командиру воинской части).</li>' +
				'<li>Вы не получали денежное довольствие (заработную плату) через ФКУ «ЕРЦ МО РФ» (в случае, если Вы недавно поступили на военную службу (работу)).</li>' +
				'<li>В единой базе данных специалистами кадрового органа некорректно введены данные для прохождения регистрации (личный номер и/или дата рождения). Для уточнения правильности введенных данных обратитесь в кадровый орган, ответственный за ввод информации в единую базу данных по Вашей воинской части, ФРП (финансово-расчетный пункт) управления (отдела) финансового обеспечения, в котором Ваша воинская часть состоит на финансовом обеспечении, или позвоните на горячую линию ФКУ «ЕРЦ МО РФ».</li>' +
			'</ol>'
		});
		container.prepend(html);

		return html;
	};

});
