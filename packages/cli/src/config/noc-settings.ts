/**
 * @license
 * Copyright 2025 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

export interface NOCSettings {
  nocSpecialization: boolean;
  defaultDomain: 'linux' | 'networking' | 'virtualization' | 'storage' | 'incident' | 'general';
  specializedPrompts: Record<string, string>;
  infrastructureContext: {
    linuxServers: string[];
    networkDevices: string[];
    virtualizationPlatforms: string[];
    storageSystems: string[];
    monitoringTools: string[];
  };
  incidentResponse: {
    escalationMatrix: Record<string, string[]>;
    slaTargets: Record<string, number>;
    runbookTemplates: string[];
  };
  automation: {
    preferredScriptingLanguage: 'bash' | 'python' | 'powershell';
    automationTools: string[];
    monitoringThresholds: Record<string, number>;
  };
}

export const DEFAULT_NOC_SETTINGS: NOCSettings = {
  nocSpecialization: true,
  defaultDomain: 'general',
  specializedPrompts: {
    linux: "You are a senior Linux system administrator with expertise in enterprise environments",
    networking: "You are a CCIE-level network engineer specializing in Cisco infrastructure",
    virtualization: "You are a virtualization expert with deep VMware and Hyper-V knowledge",
    storage: "You are a storage architect with expertise in SAN/NAS and data protection",
    incident: "You are an incident response specialist with ITIL and NOC experience"
  },
  infrastructureContext: {
    linuxServers: [
      "Red Hat Enterprise Linux",
      "CentOS",
      "Ubuntu Server",
      "SUSE Linux Enterprise Server",
      "Oracle Linux"
    ],
    networkDevices: [
      "Cisco Nexus 9000 Series",
      "Cisco Catalyst 9000 Series",
      "Cisco ISR/ASR Routers",
      "Cisco ASA Firewalls",
      "Cisco Wireless Controllers"
    ],
    virtualizationPlatforms: [
      "VMware vSphere ESXi",
      "VMware vCenter Server",
      "Microsoft Hyper-V",
      "Microsoft System Center",
      "VMware NSX"
    ],
    storageSystems: [
      "NetApp FAS/AFF",
      "EMC PowerMax",
      "HPE 3PAR",
      "Dell PowerStore",
      "Pure Storage FlashArray"
    ],
    monitoringTools: [
      "Nagios",
      "Zabbix",
      "Prometheus",
      "Grafana",
      "SolarWinds",
      "PRTG"
    ]
  },
  incidentResponse: {
    escalationMatrix: {
      "P1": ["NOC Engineer", "Senior Engineer", "Infrastructure Manager", "CTO"],
      "P2": ["NOC Engineer", "Senior Engineer", "Infrastructure Manager"],
      "P3": ["NOC Engineer", "Senior Engineer"],
      "P4": ["NOC Engineer"]
    },
    slaTargets: {
      "P1": 15, // minutes
      "P2": 60, // minutes
      "P3": 240, // minutes
      "P4": 1440 // minutes (24 hours)
    },
    runbookTemplates: [
      "Network Outage Response",
      "Server Performance Issues",
      "Storage Capacity Alert",
      "VM Failure Recovery",
      "Security Incident Response"
    ]
  },
  automation: {
    preferredScriptingLanguage: "bash",
    automationTools: [
      "Ansible",
      "Puppet",
      "Chef",
      "Terraform",
      "PowerShell"
    ],
    monitoringThresholds: {
      "cpu_usage": 80,
      "memory_usage": 85,
      "disk_usage": 90,
      "network_utilization": 75,
      "response_time": 1000 // ms
    }
  }
};

export function getNOCSettings(): NOCSettings {
  return DEFAULT_NOC_SETTINGS;
}

export function mergeNOCSettings(userSettings: Partial<NOCSettings>): NOCSettings {
  return {
    ...DEFAULT_NOC_SETTINGS,
    ...userSettings,
    specializedPrompts: {
      ...DEFAULT_NOC_SETTINGS.specializedPrompts,
      ...userSettings.specializedPrompts
    },
    infrastructureContext: {
      ...DEFAULT_NOC_SETTINGS.infrastructureContext,
      ...userSettings.infrastructureContext
    },
    incidentResponse: {
      ...DEFAULT_NOC_SETTINGS.incidentResponse,
      ...userSettings.incidentResponse
    },
    automation: {
      ...DEFAULT_NOC_SETTINGS.automation,
      ...userSettings.automation
    }
  };
}
