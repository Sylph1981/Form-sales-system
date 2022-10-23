document.addEventListener( 'wpcf7submit', function( event ) {
	switch ( event.detail.status ) {
		case 'wpcf7c_confirmed':
		wpcf7c_step1(event.detail.unitTag);
		break;
		case 'mail_sent':
		wpcf7c_step2(event.detail.unitTag);
		break;

	}
}, false );