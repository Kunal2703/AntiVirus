from django.shortcuts import render, HttpResponse
from django.template import loader
import engine
import os

# Create your views here.
def index(request):
    if request.method == 'POST':
        malware_hashes = list(open("virusHash.unibit", "r").read().split('\n'))
        finput=request.POST.get('folderInput')
        print(engine.sha256_hash(finput))
        hash_malware_check=engine.sha256_hash(finput)
        for i in malware_hashes:
            # If the file's hash matches a known malware hash, return the corresponding virus info
            if i == hash_malware_check:
                print(hash_malware_check)
                print("Virus Detected")
        return render(request, "index.html")
    else:
        return render(request, "index.html")
    