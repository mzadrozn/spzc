using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Threading;


namespace zzsnapp.Controllers
{
  [ApiController]
  [Route("[controller]")]
  public class ShortController : ControllerBase
  {
    private readonly ILogger<ShortController> _logger;
    public ShortController(ILogger<ShortController> logger)
    {
      _logger = logger;
    }

    [HttpGet(Name = "GetShort")]
    public String Get()
    {
      return "{\"from\": \"dotnetAPI\", \"message\": \"short request processed\"}";
    }
  }
}
