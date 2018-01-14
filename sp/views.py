from rest_framework.response import Response
from .serializers import MFALSerializer, SerieSerializer, PackageSerializer
from .models import MFAL, Serie, Package
from utils.views import PrivateView

class SP(PrivateView):

	def get(self, request, *args, **kwargs):
		serializer = MFALSerializer()
		return Response(serializer.data)

class CreateMFAL(PrivateView):

	def post(self, request, *args, **kwargs):
		try:
			name = request.data['name']
			mfal_code = request.data['mfal_code']
			obj = MFAL(
				name=name,
				mfal_code=mfal_code
			)
			obj.save()
			return Response({
				'id': obj.pk
			})

		except Exception as e:
			return Response({
				'error': str(e)
			})

class CreateSerie(PrivateView):

	def post(self, request, *args, **kwargs):
		try:
			name = request.data['name']
			mfal_code = request.data['mfal_code']
			ponderacion = request.data['ponderacion']
			obj = Serie(
				name=name,
				mfal_code=MFAL.objects.get(mfal_code=mfal_code),
				ponderacion=ponderacion
			)
			obj.save()
			return Response({
				'id': obj.pk
			})

		except Exception as e:
			return Response({
				'error': str(e)
			})

class CreatePackage(PrivateView):

	def post(self, request, *args, **kwargs):
		try:
			name = request.data['name']
			mfal_code = request.data['mfal_code']
			obj = Package(
				name=name,
				mfal_code=MFAL.objects.get(mfal_code=mfal_code),
			)
			obj.save()
			return Response({
				'id': obj.pk
			})

		except Exception as e:
			return Response({
				'error': str(e)
			})

class RetrieveMFAL(PrivateView):

	def get(self, request, *args, **kwargs):
		obj = MFAL.objects.all()
		serializer = MFALSerializer(obj, many=True)
		return Response(serializer.data)

class RetrieveSerie(PrivateView):

	def get(self, request, *args, **kwargs):
		obj = Serie.objects.all()
		serializer = SerieSerializer(obj, many=True)
		return Response(serializer.data)

class RetrievePackage(PrivateView):

	def get(self, request, *args, **kwargs):
		obj = Package.objects.all()
		serializer = PackageSerializer(obj, many=True)
		return Response(serializer.data)
