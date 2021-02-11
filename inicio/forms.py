from .models import Grupo, Usuario, Persona, AsignacionPersonaGrupo
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

class UserModelForm(BSModalModelForm):
    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'rol'
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'username': 'Nombre de Usuario',
            'rol': 'Rol de usuario',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'username': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control ', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'rol' :forms.Select(attrs={'class': 'form-control', 'required': True}),
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'rol'
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'username': 'Nombre de Usuario',
            'rol': 'Rol de usuario',
            'password': 'Ingrese una contraseña para el usuario'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'username': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'password': forms.PasswordInput(attrs={'class': 'form-control ', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control ', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'rol' :forms.Select(attrs={'class': 'form-control', 'required': True}),
        }

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = [
            'nombre_grupo',
            'departamento',
            'municipio',
            'identificador',
            'zona',
            'caserio',
            'canton',
            'sector',
            'aldeas',
            'paraje',
            'direccion_alternativa',
        ]
        labels = {
            'nombre_grupo':'Nombre del grupo',
            'departamento':'Departamento',
            'municipio': 'Municipio',
            'identificador':'Lugar',
            'zona':'Zona',
            'caserio':'Caserio',
            'canton':'Cantón',
            'sector':'Sector',
            'aldeas':'Aledeas',
            'paraje':'Paraje',
            'direccion_alternativa':'Direccion Alternativa',
        }
        widgets = {
            'nombre_grupo': forms.TextInput(attrs={'class': 'form-control '}),
            'departamento' :forms.Select(attrs={'class': 'form-control'}),
            'municipio' :forms.Select(attrs={'class': 'form-control'}),
            'identificador' :forms.Select(attrs={'class': 'form-control', 'onchange' : "myFunction(this.value);" }),
            'zona' :forms.Select(attrs={'class': 'form-control'}),
            'caserio' :forms.Select(attrs={'class': 'form-control'}),
            'sector' :forms.Select(attrs={'class': 'form-control'}),
            'canton' :forms.Select(attrs={'class': 'form-control'}),
            'aldeas' :forms.Select(attrs={'class': 'form-control'}),
            'paraje':forms.Select(attrs={'class': 'form-control','id':"buscar_paraje"}),
            'direccion_alternativa':forms.TextInput(attrs={'class': 'form-control '}),

        }

class GrupoModalForm(BSModalModelForm):
    class Meta:
        model = Grupo
        fields = [
            'nombre_grupo',
            'departamento',
            'municipio',
            'identificador',
            'zona',
            'caserio',
            'canton',
            'sector',
            'aldeas',
            'paraje',
        ]
        labels = {
            'nombre_grupo':'Nombre del grupo',
            'departamento':'Departamento',
            'municipio': 'Municipio',
            'identificador':'Lugar',
            'zona':'Zona',
            'caserio':'Caserio',
            'canton':'Cantón',
            'sector':'Sector',
            'aldeas':'Aledeas',
            'paraje':'Paraje',
        }
        widgets = {
            'nombre_grupo': forms.TextInput(attrs={'class': 'form-control '}),
            'departamento' :forms.Select(attrs={'class': 'form-control'}),
            'municipio' :forms.Select(attrs={'class': 'form-control'}),
            'identificador' :forms.Select(attrs={'class': 'form-control'}),
            'zona' :forms.Select(attrs={'class': 'form-control'}),
            'caserio' :forms.Select(attrs={'class': 'form-control'}),
            'sector' :forms.Select(attrs={'class': 'form-control'}),
            'canton' :forms.Select(attrs={'class': 'form-control'}),
            'aldeas' :forms.Select(attrs={'class': 'form-control'}),
            'paraje': forms.TextInput(attrs={'class': 'form-control '}),

        }

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'cui',
            'sexo',
            'primer_nombre',
            'segundo_nombre',
            'tercer_nombre',
            'primer_apellido',
            'segundo_apellido',
            'apellido_casada',
            'fecha_nacimiento',
            'telefono',
            'direccion',
            'correo_electronico',
        ]
        labels = {
            'cui': 'CUI',
            'primer_nombre': 'Primer Nombre',
            'sexo': 'Sexo',
            'segundo_nombre': 'Segundo Nombre',
            'tercer_nombre': 'Tercer Nombre',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'apellido_casada': 'Apellido Casada',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'telefono': 'Telefono',
            'direccion': 'Dirección',
            'correo_electronico': 'Correo Electronico'
        }
        widgets = {
            'cui': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control '}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control '}),
            'tercer_nombre': forms.TextInput(attrs={'class': 'form-control '}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control '}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control '}),
            'apellido_casada': forms.TextInput(attrs={'class': 'form-control '}),
            'fecha_nacimiento' :forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required': True}),
            'sexo' :forms.Select(attrs={'class': 'form-control', 'required': True}),
            'direccion': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control '}),
            'telefono': forms.TextInput(attrs={'class': 'form-control '}),
        }

class AsignacionPersonaGrupoForm(forms.ModelForm):
    class Meta:
        model = AsignacionPersonaGrupo
        fields = [
            "puesto"
        ]
        labels = {
            "puesto": "Puesto"
        }
        widgets = {
            'puesto' :forms.Select(attrs={'class': 'form-control'}),
        }

class AsignacionExistenteGrupoForm(forms.ModelForm):
    class Meta:
        model = AsignacionPersonaGrupo
        fields = [
            "persona",
            "puesto"
        ]
        labels = {
            "persona": "Persona",
            "puesto": "Puesto"
        }
        widgets = {
            'persona' :forms.Select(attrs={'class': 'form-control existente','style':"width: 100%;"}),
            'puesto' :forms.Select(attrs={'class': 'form-control'}),
        }

class AsignacionPersonaModal(BSModalModelForm):
    class Meta:
        model = AsignacionPersonaGrupo
        fields = [
            "puesto"
        ]
        labels = {
            "puesto": "Puesto"
        }
        widgets = {
            'puesto' :forms.Select(attrs={'class': 'form-control'}),
        }

class PersonaModalForm(BSModalModelForm):
    class Meta:
        model = Persona
        fields = [
            'cui',
            'sexo',
            'primer_nombre',
            'segundo_nombre',
            'tercer_nombre',
            'primer_apellido',
            'segundo_apellido',
            'apellido_casada',
            'fecha_nacimiento',
            'telefono',
            'direccion',
            'correo_electronico',
        ]
        labels = {
            'cui': 'CUI',
            'primer_nombre': 'Primer Nombre',
            'sexo': 'Sexo',
            'segundo_nombre': 'Segundo Nombre',
            'tercer_nombre': 'Tercer Nombre',
            'primer_apellido': 'Primer Apellido',
            'segundo_apellido': 'Segundo Apellido',
            'apellido_casada': 'Apellido Casada',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'telefono': 'Telefono',
            'direccion': 'Dirección',
            'correo_electronico': 'Correo Electronico'
        }
        widgets = {
            'cui': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control '}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control '}),
            'tercer_nombre': forms.TextInput(attrs={'class': 'form-control '}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control '}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control '}),
            'apellido_casada': forms.TextInput(attrs={'class': 'form-control '}),
            'fecha_nacimiento' :forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required': True}),
            'sexo' :forms.Select(attrs={'class': 'form-control', 'required': True}),
            'direccion': forms.TextInput(attrs={'class': 'form-control ', 'required': True}),
            'correo_electronico': forms.TextInput(attrs={'class': 'form-control '}),
        }
