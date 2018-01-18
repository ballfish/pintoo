from django import forms

from main.models import Commodity, Pintoo


class CommodityForm(forms.ModelForm):
    commodity = forms.CharField(label='標題', max_length=128)
    pintoo = forms.ModelChoiceField(label='類型', queryset=Pintoo.objects.all(), widget=forms.Select)
    image1 = forms.ImageField(label='圖片1', required=False)
    image2 = forms.ImageField(label='圖片2', required=False)

    class Meta:
        model = Commodity
        fields = '__all__'