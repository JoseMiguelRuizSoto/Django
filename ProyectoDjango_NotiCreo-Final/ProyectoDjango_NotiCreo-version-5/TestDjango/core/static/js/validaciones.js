$(document).ready(function() {
    // Validación personalizada para RUT chileno
    window.Parsley.addValidator('rut', {
        validateString: function(value) {
            value = value.replace('-', '-');
                if (!/^[0-9]+[-|-]{1}[0-9kK]{1}$/.test(value))
                return false;
                var tmp = value.split('-');
                var digv = tmp[1];
                var rut = tmp[0];
    
                if (digv == 'K') digv = 'k';
                    return (dv(rut) == digv);
            },
            messages: {
                es: 'El RUT no es válido.'
            }
        });
    
        function dv(T) {
            var M=0,S=1;
            for(;T;T=Math.floor(T/10))
                S=(S+T%10*(9-M++%6))%11;
            return S ? S-1 : 'k';
        }
    
        $('#rutForm').parsley();
    
        $('#btnvalida').on('click', function(event) {
            event.preventDefault(); // Para evitar el envío del formulario
            $('#rutForm').parsley().validate();
        });
        
    
    });
 
    /* add validation for minimum age */
	window.Parsley.addValidator("minimumage", {
		validateString: function(value, requirements) {
			// get validation requirments
			var reqs = value.split("-"),
				year = reqs[0],
				month = reqs[1],
				day = reqs[2];

			// check if date is a valid
			var birthday = new Date(year + "-" + month + "-" + day);

			// Calculate birtday and check if age is greater than 18
			var today = new Date();

			var age = today.getFullYear() - birthday.getFullYear();
			var m = today.getMonth() - birthday.getMonth();
			if (m < 0 || (m === 0 && today.getDate() < birthday.getDate())) {
				age--;
			}

			return age >= requirements;
		}
	});

    // Validación para contraseña (al menos 8 caracteres, al menos una mayúscula y una minúscula)
    window.Parsley.addValidator('uppercase', {
      requirementType: 'integer',
      validateString: function(value, requirement) {
        var upperCaseCount = (value.match(/[A-Z]/g) || []).length;
        return upperCaseCount >= requirement;
      },
      messages: {
        en: 'La contraseña debe contener al menos una letra mayúscula.'
      }
    });

    window.Parsley.addValidator('lowercase', {
      requirementType: 'integer',
      validateString: function(value, requirement) {
        var lowerCaseCount = (value.match(/[a-z]/g) || []).length;
        return lowerCaseCount >= requirement;
      },
      messages: {
        en: 'La contraseña debe contener al menos una letra minúscula.'
      }
    });
    