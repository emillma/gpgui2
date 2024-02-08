import type { PageLoad } from './$types.js';
export const ssr = false;

export const load: PageLoad = ({ params, url }) => {
    return {
        title: `Title for ${params.program} goes here`,
        content: `Content for ${params.program} goes here or here`
    };
};
