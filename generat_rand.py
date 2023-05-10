#!/bin/python
print("generiere")

for i in range(0,30):            
    print(str(4096+(i*16)) + ":" + hex(126))
    print(str(4097+(i*16)) + ":" + hex(126))
    print(str(4098+(i*16)) + ":" + hex(126))

    print(str(4104+(i*16)) + ":" + hex(126))
    print(str(4105+(i*16)) + ":" + hex(126))
    print(str(4106+(i*16)) + ":" + hex(126))

    print(str(4096 + (19*480) +(i*16)) + ":" + hex(126))
    print(str(4097+ (19*480) +(i*16)) + ":" + hex(126))
    print(str(4098+ (19*480) +(i*16)) + ":" + hex(126))

    print(str(4104+ (19*480)+(i*16)) + ":" + hex(126))
    print(str(4105+ (19*480)+(i*16)) + ":" + hex(126))
    print(str(4106+ (19*480)+(i*16)) + ":" + hex(126))
          

for i in range(0, 20):
    print(str(4096+(i*480)) + ":" + hex(126))
    print(str(4097+(i*480)) + ":" + hex(126))
    print(str(4098+(i*480)) + ":" + hex(126))
          
    print(str(4104+(i*480)) + ":" + hex(126))
    print(str(4105+(i*480)) + ":" + hex(126))
    print(str(4106+(i*480)) + ":" + hex(126))
          
    print(str(4096+ 464 +(i*480)) + ":" + hex(126))
    print(str(4097+ 464+(i*480)) + ":" + hex(126))
    print(str(4098+ 464+(i*480)) + ":" + hex(126))
          
    print(str(4104+ 464 +(i*480)) + ":" + hex(126))
    print(str(4105+ 464 +(i*480)) + ":" + hex(126))
    print(str(4106+ 464 +(i*480)) + ":" + hex(126))
          
