import type { PageLoad } from './$types.js';
export const ssr = false;

export const load: PageLoad = ({ params, url }) => {
    return {
        title: `Title for ${params.slug} goes here`,
        content: `Content for ${params.slug} goes here or here`
    };
};
