from app001.models import Flowchart,Flowchartprocess

processes = Flowchartprocess.objects.all()

for p in processes:
    print(p)
