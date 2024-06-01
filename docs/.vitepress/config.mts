import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "CISCAPPS",
  description: "A KioydioLabs product.",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Introduction',
        link: '/introduction',
      },
      {
        text: 'Docker Installation',
        link: '/docker-installation',
        collapsed: true,
        items: [
          { text: 'Installing requirements', link: '/installing-requirements' },
          { text: 'Modify the configuration file', link: '/modify-configuration-file' },
          { text: 'Deploy CISCAPPS', link: '/deploy-ciscapps' }
        ]
      },
      {
        text: 'Deskphone Configuration',
        link: '/deskphone-configuration',
        collapsed: true,
        items: [
            { text: 'FreePBX Configuration', link: '/free-pbx-configuration' },
            { text: 'XML File Configuration (Manual)', link: '/xml-file-manual-configuration' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
