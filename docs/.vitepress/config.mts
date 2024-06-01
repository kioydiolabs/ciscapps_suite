import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "CISCAPPS",
  description: "OpenSource web apps for Cisco IP deskphones created by KioydioLabs.",
  head: [
    ['link', { rel: 'icon', href: '/logo.jpg' }],
    ['meta', { name: 'theme-color', content: '#007bdf' }]
  ],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    search: {
      provider: 'local'
    },
    logo: '/logo.jpg',
    nav: [
      { text: 'Home', link: '/' }
    ],
    footer: {
      message: 'Released under the BSD 3-Clause License',
      copyright: 'KIOYDIOLABS © 2024'
    },
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
      { icon: 'github', link: 'https://github.com/kioydiolabs/ciscapps_suite' }
    ]
  }
})
