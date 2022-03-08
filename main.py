import yaml
from datetime import datetime, timedelta
now = datetime.now()
with open(r'C:\Users\MANASA\Desktop\KLA-\kla.yaml') as f:
    yaml_content = yaml.safe_load(f)

    def seqfunction(activity, name, f1, rname):
        global now
        # ~f1 = open("klaout.txt", "w")
        for key in activity:
            object = activity[key]
            if(rname == "None"):
                printobj = ";" + name+"."+key+" "
            else:
                printobj = ";" + name+"."+rname+"."+key+" "
            fWriteOp = str(now)+printobj+"Entry\n"
            f1.write(fWriteOp)
            fl = 1
            for j in object:
                if(j == "Inputs"):
                    fl = 0
            if(fl == 0):
                # only if its a executable function
                inputs = object['Inputs']
                fname = object['Function']
                time = inputs['ExecutionTime']
                fWriteOp = ""
                # write the output to fsile
                fWriteOp = str(now)+printobj+"Executing " + \
                    fname+" ("+inputs['FunctionInput']+", "+time+")\n"
                f1.write(fWriteOp)
                now = now + timedelta(seconds=int(time))
                #now += timedelta(seconds=int(time))
                fWriteOp = ""
                fWriteOp = str(now)+printobj+"Exit\n"
                f1.write(fWriteOp)
            else:
                seqfunction(object['Activities'], name, f1, key)
                #f1.write("In process \n")
                # write the output to f
                fWriteOp = ""
                fWriteOp = str(now)+printobj+"Exit\n"
                f1.write(fWriteOp)
    f1 = open("output.txt", "w")
    mainyaml_content = yaml_content['M1A_Workflow']
    name = "M1A_Workflow"
    fobj = str(now)+";"+name+" Entry\n"
    f1.write(fobj)
    for key in mainyaml_content:
        if mainyaml_content[key] == 'Sequential':
            stri = "None"
            seqfunction(mainyaml_content['Activities'], name, f1, stri)
            fWriteOp = ""
            fWriteOp = str(now)+";"+name+" Exit\n"
            f1.write(fWriteOp)
        # else:
            # concurrentfunction(mainyaml_content['Activities'])
            # print(yaml_content['M1SampleSubTask1']['Task'])
            # print(yaml_content['M1A_Workflow']['M1SampleSubFlow']['M1SampleSubTask1'])