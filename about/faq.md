---
title: FAQ
layout: info
---

## {{ page.title }}
{: .page-header .no_toc}

*These FAQs primarily target Sandia developers working in the [SandiaLabs GitHub organization](https://github.com/sandialabs). Don't see your question listed below? Please contact [SandiaLabs GitHub admins](mailto:wg-1424-ops@sandia.gov).*

* Table of Contents
{:toc}

### How do I set up a GitHub account?

If you’re new to GitHub and open source in general, figuring out how to get set up can be a challenge. You may want to read through the GitHub Help pages on [setting up and managing your GitHub profile](https://help.github.com/categories/setting-up-and-managing-your-github-profile/).

1. [Create an account on GitHub](https://github.com/join).

    You *do not need* a separate work account and personal account. Instead, you can [link multiple email addresses to the same GitHub account](https://help.github.com/articles/adding-an-email-address-to-your-github-account/), which is almost always preferred.

2. [Update your profile information](https://github.com/settings/profile).

    * **Photo**: A headshot photo, or image that is uniquely you.
    * **Name**: Your first and last name.
    * **Bio**: Include a few words about yourself!
    * **URL**: This might be a personal website.
    * **Company**: Probably `Sandia National Labs`.
    * **Location**: Your primary location.

3. Add your `@sandia.gov` email address (and any aliases) to your [Email Settings](https://github.com/settings/emails) page. This will link any commits done via [your Git identity](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup#Your-Identity) to your GitHub account.

4. [Enable two-factor authentication (2FA)](https://github.com/settings/security).

### How do I join the SandiaLabs organization on GitHub?

If you are an employee at Sandia, you are eligible to join the [SandiaLabs GitHub organization](https://github.com/sandialabs) and appear in the [member list](https://github.com/orgs/sandialabs/people).

1. Send an email, with your GitHub username included, to the [SandiaLabs GitHub admins](mailto:wg-1424-ops@sandia.gov) from your `@sandia.gov` email, requesting to be added to the organization.

2. After an administrator has added you to the organization, you will receive a notification email from GitHub. Alternatively, once the invitation has been sent, you will see a notification banner at the top of [github.com/sandialabs](https://github.com/sandialabs) which you can use to accept the invitation.

3. Head over to the [SandiaLabs People](https://github.com/orgs/sandialabs/people) page and make your membership `Public`.


### What is/isn’t allowed to be included in my repo?

Remember that these repositories *are hosted* on GitHub servers, *NOT Sandia servers*, and content placed in them should be limited to "email like" communications. That means:

* NO Classified
* NO Export Controlled
* NO Official Use Only (OUO)
* NO Health Insurance Portability and Accountability Act (HIPAA)
* NO Personally Identifiable Information (PII)
* NO NDA or vendor-proprietary information
* NO Unclassified Controlled Information (UCI)
* NO Unclassified Controlled Nuclear Information (UCNI)

When in doubt, contact a Derivative Classifier (DC) for further guidance.


### How do I include my repo in the Sandia organization and/or this website’s catalog?

Repositories within the SandiaLabs organization are owned and managed by Sandia. Please do not create personal repositories here.

Make sure your repository is included on this website’s home page and [full catalog](https://software.sandia.gov/). If you’ve set up your repository within the SandiaLabs organization, you don’t need to take any action; it will automatically appear after the next data update.

* If your repository exists under a different organization, you can move it to SandiaLabs by selecting “Transfer Ownership” under Settings.

* Alternatively, you can submit a pull request [updating the `input_lists.json` file](https://github.com/sandialabs/sandialabs.github.io/blob/master/_explore/input_lists.json), with your organization and/or repository names.

* If you have a project logo, please follow the [instructions](https://github.com/sandialabs/sandialabs.github.io/tree/master/assets/images/logos) for naming and uploading the file. If your repo is part of a non-Sandia organization that has its own avatar, that image will automatically display next to the repo name in the catalog, unless superseded by a repo-specific logo.


### How do I contribute news or other content to this website?

Submit a pull request! This website is a GitHub repo just like any other Sandia open source project. News is housed in the [`_posts` directory](https://github.com/sandialabs/sandialabs.github.io/tree/master/_posts), and templates are found in the [sandialabs/.github repo](https://github.com/sandialabs/.github). See the guidelines below about contributing.

Before contributing, please contact [wg-1424-ops@sandia.gov](mailto:wg-1424-ops@sandia.gov) with your idea or if you have questions about whether your proposed content requires the Sandia review and release process.

### What should I do if my repo is no longer actively developed/maintained?

1. Remove your repo’s topic tags (e.g., `math-physics`), which connect it to this website’s browsable categories. 

2. Submit a pull request [updating the `input_lists.json` file](https://github.com/sandialabs/sandialabs.github.io/blob/master/_explore/input_lists.json) to remove your repo’s name.

3. Change your repo's status via Settings > Manage Access > Who has access > Manage > Danger Zone > Archive this repository (`settings#danger-zone`). Contact [wg-1424-ops@sandia.gov](mailto:wg-1424-ops@sandia.gov) if for some reason GitHub won't let you complete this step.

