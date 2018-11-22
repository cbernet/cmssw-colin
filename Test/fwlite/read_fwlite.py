import ROOT
ROOT.gROOT.SetBatch()

from DataFormats.FWLite import Events, Handle

# events = Events('root://cms-xrd-global.cern.ch//store/mc/RunIIFall17MiniAODv2/VBFHToTauTau_M125_13TeV_powheg_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/549B2DC8-C443-E811-9DAF-A0369FE2C17C.root')
events = Events('test.root')

# handle  = Handle ('std::vector<pat::Electron>')
handle = Handle('edm::View<pat::Electron>')

for i,event in enumerate(events): 
    event.getByLabel(('slimmedElectrons'),handle)
    import pdb; pdb.set_trace()
    for i in range(len(handle)):
        eleptr = handle.ptrAt(i)
        print eleptr
    electrons = handle.product()
    if not len(electrons):
        continue
    import pdb; pdb.set_trace()
    if i==100: 
        break

