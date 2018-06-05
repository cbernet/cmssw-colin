# Colin's private CMSSW subsystem

## Installation

Initialize your CMS environment

```
cd $CMSSW_BASE
git clone https://github.com/cbernet/cmssw-colin.git Colin 
scram b -j 4
```

## Components

### Common / cfg 

Simple cmsRun configuration scripts showing e.g. how to: 
 - pick events from a set of input files 
 - merge a set of input files 
 - ... 
