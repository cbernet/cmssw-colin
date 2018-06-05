import FWCore.ParameterSet.Config as cms

##____________________________________________________________________________||
process = cms.Process("MERGE")

##____________________________________________________________________________||
process.load("FWCore.MessageLogger.MessageLogger_cfi")

list_of_files = []

##____________________________________________________________________________||
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        list_of_files
        )
    )

##____________________________________________________________________________||
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('merge.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    outputCommands = cms.untracked.vstring(
        'keep *'
        )
    )

##____________________________________________________________________________||
process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
process.MessageLogger.cerr.FwkReport.reportEvery = 50
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))


##____________________________________________________________________________||
process.p = cms.Path()

process.e1 = cms.EndPath(
    process.out
    )

##____________________________________________________________________________||

