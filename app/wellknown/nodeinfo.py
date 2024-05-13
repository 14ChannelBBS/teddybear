from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..config import Config

router = APIRouter()

@router.get("/.well-known/nodeinfo")
async def nodeinfo():
	return {
		"links": [
			{
			"rel": "http://nodeinfo.diaspora.software/ns/schema/2.1",
			"href": f"https://{Config.serverAddress}/nodeinfo/2.1"
			},
			{
			"rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
			"href": f"https://{Config.serverAddress}/nodeinfo/2.0"
			}
		]
	}

@router.get("/nodeinfo/2.1")
async def nodeinfo():
	return {
		"version": "2.1",
		"software": {
			"name": "teddybear",
			"version": Config.softwareVersion,
			"homepage": "https://github.com/14ChannelBBS/teddybear",
			"repository": "https://github.com/14ChannelBBS/teddybear"
		},
		"protocols": [
			"activitypub"
		],
		"services": {
			"inbound": [],
			"outbound": [
				"atom1.0",
				"rss2.0"
			]
		},
		"openRegistrations": Config.openRegistrations,
		"usage": {
			"users": {
				"total": 0,
				"activeHalfyear": None,
				"activeMonth": None
			},
			"localPosts": 0,
			"localComments": 0
		},
		"metadata": {
			"nodeName": Config.nodeName,
			"nodeDescription": Config.nodeDescription,
			"nodeAdmins": Config.nodeAdmins,
			"maintainer": Config.maintainer,
			"langs": Config.langs,
			"tosUrl": Config.tosUrl,
			"privacyPolicyUrl": Config.privacyPolicyUrl,
			"impressumUrl": Config.impressumUrl,
			"repositoryUrl": "https://github.com/14ChannelBBS/teddybear",
			"feedbackUrl": "https://github.com/14ChannelBBS/teddybear/issues/new",
			"disableRegistration": Config.disableRegistration,
			"disableLocalTimeline": Config.disableLocalTimeline,
			"disableGlobalTimeline": Config.disableGlobalTimeline,
			"emailRequiredForSignup": Config.emailRequiredForSignup,
			"enableHcaptcha": Config.enableHcaptcha,
			"enableRecaptcha": Config.enableRecaptcha,
			"enableMcaptcha": Config.enableMcaptcha,
			"enableTurnstile": Config.enableTurnstile,
			"maxNoteTextLength": Config.maxNoteTextLength,
			"enableEmail": Config.enableEmail,
			"enableServiceWorker": Config.enableServiceWorker,
			"proxyAccountName": Config.proxyAccountName,
			"themeColor": Config.themeColor
		}
	}

@router.get("/nodeinfo/2.0")
async def nodeinfo():
	return {
		"version": "2.1",
		"software": {
			"name": "teddybear",
			"version": Config.softwareVersion,
			"homepage": "https://github.com/14ChannelBBS/teddybear"
		},
		"protocols": [
			"activitypub"
		],
		"services": {
			"inbound": [],
			"outbound": [
				"atom1.0",
				"rss2.0"
			]
		},
		"openRegistrations": Config.openRegistrations,
		"usage": {
			"users": {
				"total": 0,
				"activeHalfyear": None,
				"activeMonth": None
			},
			"localPosts": 0,
			"localComments": 0
		},
		"metadata": {
			"nodeName": Config.nodeName,
			"nodeDescription": Config.nodeDescription,
			"nodeAdmins": Config.nodeAdmins,
			"maintainer": Config.maintainer,
			"langs": Config.langs,
			"tosUrl": Config.tosUrl,
			"privacyPolicyUrl": Config.privacyPolicyUrl,
			"impressumUrl": Config.impressumUrl,
			"repositoryUrl": "https://github.com/14ChannelBBS/teddybear",
			"feedbackUrl": "https://github.com/14ChannelBBS/teddybear/issues/new",
			"disableRegistration": Config.disableRegistration,
			"disableLocalTimeline": Config.disableLocalTimeline,
			"disableGlobalTimeline": Config.disableGlobalTimeline,
			"emailRequiredForSignup": Config.emailRequiredForSignup,
			"enableHcaptcha": Config.enableHcaptcha,
			"enableRecaptcha": Config.enableRecaptcha,
			"enableMcaptcha": Config.enableMcaptcha,
			"enableTurnstile": Config.enableTurnstile,
			"maxNoteTextLength": Config.maxNoteTextLength,
			"enableEmail": Config.enableEmail,
			"enableServiceWorker": Config.enableServiceWorker,
			"proxyAccountName": Config.proxyAccountName,
			"themeColor": Config.themeColor
		}
	}