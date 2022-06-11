using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Threading;

namespace spzcapp.Controllers
{
  [ApiController]
  [Route("")]
  public class RootController
  {
    private readonly ILogger<RootController> _logger;
    public RootController(ILogger<RootController> logger)
    {
      _logger = logger;
    }

    [HttpGet(Name = "Get")]
    public String Get()
    {
      return "I'm alive - .NET API :)";
    }
  }
}
