#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2016 VMware, Inc.  All rights reserved. -- VMware Confidential

"""
Gobuild components consumed by vRealize VA.
"""

CSC_PHOTON_BRANCH = 'photon3-vmw-updates'
CSC_PHOTON_CLN = 9176122
CSC_PHOTON_BUILDTYPE = 'release'
CSC_PHOTON_DELIVERABLE = [r'publish/csc-photon-3.0.0-x86_64.*\.iso$',
                          r'publish/csc-photon-3.0.0-x86_64\.pkginfo\.txt$'
                          ]
CSC_PHOTON_FILES = {'linux64-vm': CSC_PHOTON_DELIVERABLE}

VA_BUILD_BRANCH = 'main'
VA_BUILD_CLN = 786798
VA_BUILD_BUILDTYPE = 'release'
VA_BUILD_HOSTTYPES = {'linux64-vm': 'linux'}

VA_HARDENING_BRANCH = 'vahardening-photon'
VA_HARDENING_CLN = 670390
VA_HARDENING_BUILDTYPE = 'release'
VA_HARDENING_DELIVERABLE = [r'publish/photon_hardening.*$']
VA_HARDENING_FILES = {'linux64-vm': VA_HARDENING_DELIVERABLE}


# Cayman OpenJDK
CAYMAN_OPENJDK_BRANCH = 'vmware-prebuilt-jdk11'
CAYMAN_OPENJDK_CLN = '46dc111ab3b152860b3b2602d52705da68c8da9e'
CAYMAN_OPENJDK_BUILDTYPE = 'release'
CAYMAN_OPENJDK_DELIVERABLE = {
    'linux64-vm': [r'publish/lin64/rpm-4.4.2/vmware-jre-11.*.x86_64.rpm', r'publish/win64/jre', ],
    'linux64': [r'publish/lin64/rpm-4.4.2/vmware-jre-11.*.x86_64.rpm', r'publish/win64/jre', ]
}

# Remove oracle JRE to claim full OpenJDK support
# Lcmagent either will be removed ( if support drops 8.2) or compatibility
# to be checked with OpenJDK JRE which will be currently packaged
# JDK_BRANCH = 'cayman_openjdk'
# JDK_CLN = '6fd6f048c468cf291cb8a9849f650ffefe34c9f0'
# JDK_BUILDTYPE = 'release'
# JDK_DELIVERABLE = {
#     'linux64-vm': [ r'publish/server-jre-redist/vmware-jre-1.8.*server.x86_64.rpm', r'publish/jre-redist/jre-1.8.*-win64\.zip$', ],
#     'linux64': [ r'publish/server-jre-redist/vmware-jre-1.8.*server.x86_64.rpm', r'publish/jre-redist/jre-1.8.*-win64\.zip$', ],
# }


STUDIOVA_BRANCH = 'master'
STUDIOVA_CLN = '3990636c0105754e92eb58162eaff7cfb463870a'
STUDIOVA_BUILDTYPE = 'release'
STUDIOVA_DELIVERABLE = [r'publish/prod/exports/ova/.*.ova$']

STUDIOVA_FILES = {'linux64': STUDIOVA_DELIVERABLE,
                  'linux64-vm': STUDIOVA_DELIVERABLE,
                  'linux': STUDIOVA_DELIVERABLE}


VRLCM_SERVICECOMPOSER_BRANCH = 'master'
VRLCM_SERVICECOMPOSER_CLN = '5f84e394d2ea9fd47f2f1dcd01b4ed83fa66c98d'
VRLCM_SERVICECOMPOSER_BUILDTYPE = 'release'
VRLCM_SERVICECOMPOSER_FILES = {'linux64-vm': [r'publish/*']}

# do not change postgres version it will start breaking upgrade. Handel data transfer from one version from another:wq1
VPOSTGRES_DBVM_CLN = '7a1af7a1e1f95c4f05ca28c91cd8de3458dbaf43'
VPOSTGRES_DBVM_BRANCH = 'REL_11_STABLE'
VPOSTGRES_DBVM_BUILDTYPE = 'release'
VPOSTGRES_DBVM_FILES = {'linux64-vm': [
    r'publish/VMware-Postgres-11\..*\.x86_64\.rpm',
    r'publish/VMware-Postgres-contrib-.*\.x86_64\.rpm',
    r'publish/VMware-Postgres-extras-init-.*\.x86_64\.rpm',
    r'publish/VMware-Postgres-extras-.*\.x86_64\.rpm',
    r'publish/VMware-Postgres-osslibs-.*\.x86_64\.rpm',
    r'publish/VMware-Postgres-pg_top-.*\.x86_64\.rpm',
    r'publish/VMware-Postgres-libs-.*\.x86_64\.rpm',
    r'publish/VMware-Postgres-server-.*\.x86_64\.rpm',
    r'publish/VMware-Postgres-odbc-.*\.x86_64\.rpm',
]}

# vmtools-prod	vmware tools
TOOLS_BRANCH = 'vmtools-prod'
TOOLS_BUILDTYPE = 'release'
TOOLS_CLN = '4514099'
TOOLS_FILES = \
    {'linux64-vm': [r'publish/windows.iso']}

# vrlcm-agents
VRLCM_AGENTS_BRANCH = 'master-rel'
VRLCM_AGENTS_BUILDTYPE = 'release'
VRLCM_AGENTS_CLN = '7b65f2665fe1c527626fdb4adbe34951f8330566'
VRLCM_AGENTS_FILES = \
    {'linux64-vm': [r'publish/lcm-agent.zip']}

# apuat-paks 7.5.0
VROPS_APUAT75_BRANCH = 'mi-vcops-suite-vm-main'
VROPS_APUAT75_BUILDTYPE = 'release'
VROPS_APUAT75_CLN = '1260237'
VROPS_APUAT75_FILES = \
    {'linux64-vm': [r'publish/.*.pak']}


# apuat-paks 8.0.1
VROPS_APUAT80_BRANCH = 'mi-vcops-suite-vm-800'
VROPS_APUAT80_BUILDTYPE = 'release'
VROPS_APUAT80_CLN = '1411855'
VROPS_APUAT80_FILES = \
    {'linux64-vm': [r'publish/.*.pak']}

# apuat-paks 8.1.0
VROPS_APUAT81_BRANCH = 'mi-vcops-suite-vm-810'
VROPS_APUAT81_BUILDTYPE = 'release'
VROPS_APUAT81_CLN = '1465504'
VROPS_APUAT81_FILES = \
    {'linux64-vm': [r'publish/.*.pak']}

# apuat-paks 8.1.1
VROPS_APUAT811_BRANCH = 'mi-vcops-suite-vm-811'
VROPS_APUAT811_BUILDTYPE = 'release'
VROPS_APUAT811_CLN = '1523099'
VROPS_APUAT811_FILES = \
    {'linux64-vm': [r'publish/.*.pak']}


# apuat-paks 8.2.0
VROPS_APUAT820_BRANCH = 'v8.2.0'
VROPS_APUAT820_BUILDTYPE = 'release'
VROPS_APUAT820_CLN = '1587596'
VROPS_APUAT820_FILES = \
    {'linux64-vm': [r'publish/.*.pak']}

# apuat-paks 8.3.0
VROPS_APUAT830_BRANCH = 'v8.3.0'
VROPS_APUAT830_BUILDTYPE = 'release'
VROPS_APUAT830_CLN = '1652583'
VROPS_APUAT830_FILES = \
    {'linux64-vm': [r'publish/.*.pak']}


# apuat-paks 8.4.0
VROPS_APUAT840_BRANCH = 'v8.4.0'
VROPS_APUAT840_BUILDTYPE = 'release'
VROPS_APUAT840_CLN = '1688181'
VROPS_APUAT840_FILES = \
    {'linux64-vm': [r'publish/.*.pak']}


# apuat-paks 8.5.0
VROPS_APUAT850_BRANCH = 'v8.5.0'
VROPS_APUAT850_BUILDTYPE = 'release'
VROPS_APUAT850_CLN = '1703021'
VROPS_APUAT850_FILES = \
    {'linux64-vm': [r'publish/.*.pak']}

# VMware-Log-Insight-Agent
STRATA_AGENT_CLN = '6a619b574532f3fe7a3a0d1ef6bc10c24a45c09d'
STRATA_AGENT_BRANCH = 'release/8.2-ga'
STRATA_AGENT_BUILDTYPE = 'release'
STRATA_AGENT_FILES = \
    {'linux64-vm': [r'publish/VMware-Log-Insight-Agent-.*\.rpm']}

VRLCM_SERVICES_BRANCH = 'vrlcm-84-GA-patch1'
VRLCM_SERVICES_CLN ='acd146c269660f48b195eec41b259908c24dc3c9'
VRLCM_SERVICES_BUILDTYPE = 'release'
VRLCM_SERVICES_FILES = {'linux64-vm': [r'publish/']}

# blackstone
VREALIZE_BLACKSTONE_BRANCH = 'mana-rel'
VREALIZE_BLACKSTONE_CLN = '227826299e4d4f47679a735b3f98b9a084b1a8de'
VREALIZE_BLACKSTONE_BUILDTYPE = 'release'
VREALIZE_BLACKSTONE_DELIVERABLE = {
    'linux64-vm': [r'publish/blackstone.zip'],
    'linux64': [r'publish/blackstone.zip']
}

# telemetry
TELEMETRY_BRANCH = 'vrslcm'
TELEMETRY_BUILDTYPE = 'release'
TELEMETRY_CLN = '26eb1e3ef236940415651de6f60cc32a3e29f8dc'
TELEMETRY_FILES = \
    {'linux64-vm': [r'publish/telemetry-collector.*\.noarch\.rpm']}

# vidm cluster support
VIDM_VA_333_BRANCH = '2018q3-vra-8'
VIDM_VA_333_BUILDTYPE = 'release'
VIDM_VA_333_CLN = '64d305b2ba5dd26eefd955debc573a930fef795c'
VIDM_VA_333_FILES = {'linux64-vm': [r'publish/cluster/.*\.tgz']}
