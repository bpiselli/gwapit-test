import { GwapitWebPage } from './app.po';

describe('gwapit-web App', () => {
  let page: GwapitWebPage;

  beforeEach(() => {
    page = new GwapitWebPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
